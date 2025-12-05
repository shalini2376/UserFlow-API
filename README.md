## 🧩 UserFlow API

A clean and modular User Management Backend Service built using Python Flask and SQLite.
UserFlow API provides secure authentication, complete CRUD operations, search functionality, and well-structured JSON responses.
Designed as a lightweight backend microservice following clean API design principles.

## 🔗 Live API (Render Deployment)

👉 https://retainsure-task-1.onrender.com

## 🚀 Features

## 🔧 1. Complete User CRUD

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| GET    | `/users`      | Fetch all users   |
| GET    | `/users/<id>` | Fetch single user |
| POST   | `/users`      | Create new user   |
| PUT    | `/users/<id>` | Update user       |
| DELETE | `/user/<id>`  | Delete user       |


## 🔍 2. Search Users

Search users by name:

- GET /search?name=john

## 🔐 3. Authentication

- Login using hashed password verification:

👉 POST /login  
{  
  "email": "user@example.com",  
  "password": "mypassword"  
}  
Password hashing via Werkzeug Security.

##  ⚙️ 4. Database Layer

- SQLite-powered storage

- Safe parameterized queries

- Automatic connection handling via get_db_connection()

## 🛡 5. Strong Error Handling

Covers:

- Missing fields

- Invalid credentials

- User not found

- SQL errors

- Unexpected exceptions

Returns correct HTTP status codes such as 200, 201, 400, 401, 404, 500.

## 🛠 Tech Stack

- Python 3
- Flask
- SQLite
- Werkzeug Security
- REST API Architecture

## 📁 Project Structure

```
├── app.py
├── init_db.py
├── users.db
├── requirements.txt
└── README.md

```

## ▶️ How to Run Locally

1️⃣ Clone the repository
git clone https://github.com/shalini2376/userflow-api  
cd userflow-api  

2️⃣ Create virtual environment (optional)
python -m venv venv  
venv\Scripts\activate           # Windows  

3️⃣ Install dependencies
pip install -r requirements.txt  

4️⃣ Initialize the database  
python init_db.py  

5️⃣ Start the server  
python app.py   

## 🟢 Server is available at:
http://127.0.0.1:5009

## 📌 API Usage Examples

➕ Create User

POST /users
{  
  "name": "Alice",  
  "email": "alice@example.com",  
  "password": "mypassword"  
}  

## 🔍 Get All Users
GET /users

🔎 Search Users  
GET /search?name=al  

## 🔐 Login
POST /login 
{  
  "email": "alice@example.com",  
  "password": "mypassword"  
}  
  
## 🧪 API Testing (.http file | VSCode REST Client)

Use this block inside a .http file to test all endpoints:

### Home route  
GET http://localhost:5009/  

### Get all users  
GET http://localhost:5009/users    

### Get a single user  
GET http://localhost:5009/users/2  

### Create a user  
POST http://localhost:5009/users  
Content-Type: application/json  

{  
  "name": "Shalini",  
  "email": "shalini@example.com",  
  "password": "abc123"  
}

### Update a user  
PUT http://localhost:5009/users/4  
Content-Type: application/json  

{
  "name": "Updated Shalini",  
  "email": "newemail@example.com",  
  "password": "abc123"  
}

### Delete a user  
DELETE http://localhost:5009/user/6  

### Login  
POST http://localhost:5009/login  
Content-Type: application/json  

{  
  "email": "shalini@example.com",  
  "password": "abc123"  
}

## 🌟 What I Learned

- Building REST APIs in Flask

- Managing databases using SQLite

- Implementing secure password hashing & login

- Writing clean, modular backend code

- Handling errors and returning appropriate HTTP status codes

- Testing APIs using .http files and REST clients
