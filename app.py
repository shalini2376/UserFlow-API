from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from init_db import get_db_connection

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "User Management System"

# get allUsers
@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        conn, cursor = get_db_connection()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return jsonify(users), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

# get a single user based on ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        conn, cursor = get_db_connection()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = cursor.fetchone()
        conn.close()

        if user:
            return jsonify(user), 200
        else:
            return jsonify({"error": "User not found"}), 404

    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


# create a user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        request_data = request.get_json()
        user_name = request_data.get('name')
        user_email = request_data.get('email')
        password = request_data.get('password')
        hashed_password = generate_password_hash(password)

        if not all([user_name, user_email, password]):
            return jsonify({"error": "Missing data"}), 400

        conn, cursor = get_db_connection()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (user_name, user_email, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({"message": "User created successfully"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500 


# Update a User
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    try:
        data = request.get_json()
        user_name = data.get('name')
        user_email = data.get('email')
        password = data.get('password')
        hashed_password = generate_password_hash(password)

        if not all([user_name, user_email, password]):
            return jsonify({"error": "Missing data"}), 400

        conn, cursor = get_db_connection()
        cursor.execute("UPDATE users SET name=?, email=?, password=? WHERE id=?", (user_name, user_email, hashed_password, user_id))
        conn.commit()

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({"error": "User not found"}), 404

        conn.close()
        return jsonify({"message": "User updated successfully"}), 200
    
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500 
   

    
# Delete a user
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    try:
        conn, cursor = get_db_connection()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({"error": "user not found"}), 404  

        conn.commit()
        conn.close()                          
    
        print(f"User {user_id} deleted")
        return jsonify({"message": "User deleted successfully"}), 200
    
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}),500
    except Exception as e:
        return jsonify({"error": f"Unexpected Error {str(e)}"}), 500

# search a User by name
@app.route('/search', methods=['GET'])
def search_users_by_name():
    try:
        user_name = request.args.get('name')

        if not user_name:
            return jsonify({"error": "Please provide a name to search"}), 400

        conn, cursor = get_db_connection()
        cursor.execute("SELECT * FROM users WHERE name LIKE ?", (f'%{user_name}%',))
        users = cursor.fetchall()
        conn.close()

        if not users:
            return jsonify({"message": "No users found"}), 404

        return jsonify(users), 200

    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

# login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user_email = data.get('email')
        user_password = data.get('password')

        if not user_email or not user_password:
            return jsonify({"error": "Email and password are required"}), 400

        conn, cursor = get_db_connection()
        cursor.execute("SELECT id, password FROM users WHERE email = ? ", (user_email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[1], user_password):
            return jsonify({"status": "success", "user_id": user[0]}), 200
        else:
            return jsonify({"status": "failed", "message": "Invalid credentials"}), 401

    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)