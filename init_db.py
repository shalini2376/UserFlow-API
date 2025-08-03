import sqlite3

def get_db_connection():
    conn = sqlite3.connect('users.db', check_same_thread=False)
    cursor = conn.cursor()
    return conn, cursor

if __name__ == "__main__":
    conn, cursor = get_db_connection()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    cursor.execute("INSERT INTO users (name, email, password) VALUES ('John Doe', 'john@example.com', 'password123')")
    cursor.execute("INSERT INTO users (name, email, password) VALUES ('Jane Smith', 'jane@example.com', 'secret456')")
    cursor.execute("INSERT INTO users (name, email, password) VALUES ('Bob Johnson', 'bob@example.com', 'qwerty789')")

    conn.commit()
    conn.close()

print("Database initialized with sample data")