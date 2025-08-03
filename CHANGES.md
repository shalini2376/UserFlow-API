# Flask User Management System – Refactoring Summary

This project focuses on enhancing a basic Flask-based User Management API by identifying critical flaws, applying essential security and architecture improvements, and keeping changes within scope constraints.

---

## Major Issues Identified

1. **Plaintext Passwords**  
   - Passwords were stored and validated in plaintext, exposing users to high risk if the database is compromised.

2. **SQL Injection Vulnerability**  
   - Dynamic SQL strings like `f"SELECT * FROM users WHERE id = '{user_id}'"` allowed injection attacks.

3. **Unsafe Input Handling**  
   - Directly parsing `request.get_data()` and trusting all input values without checks.

4. **No Error Handling or Status Codes**  
   - Most endpoints returned plain strings without consistent HTTP status codes.

5. **Inconsistent API Structure**  
   - Routes were poorly named or lacked RESTful conventions (e.g., `/user/<id>` vs `/users/<id>`).

6. **Open and Persistent DB Connection**  
   - A single global connection (`check_same_thread=False`) was used across all requests, risking race conditions and performance issues.

7. **Improper Login Logic**  
   - Login endpoint exposed raw user data and lacked proper authentication flow.

---

## Changes Made and Why

| Change - Reason |
1. Replaced global DB connection with `get_db_connection()`
    - Prevent threading issues and promote clean connection handling

2. Used parameterized SQL queries (`?`)
    - Prevent SQL injection attacks

3. Applied `generate_password_hash` and `check_password_hash`
    - Enforce secure password storage and comparison.

4. Added input validation checks
    - Prevents crashes due to missing or malformed fields

5. Standardized route paths
    - Ensured RESTful route naming (`/users/<id>`, `/search`, `/login`)

6. Implemented detailed error handling and status codes
    - Ensures consistent API communication and debugging

7. Returned `jsonify()` responses everywhere
    - Unified response format for frontend/API consumption 
    
8. Create and use the app.http file 
    - to send HTTP requests and test the API endpoints during development.


## Assumptions and Trade-offs 

- **No session management or tokens**  
  Passwords are validated but no login session or JWT is returned, assuming the scope is limited to basic credential verification.

- **Tuple-based row access**  
  Continued using `user[0]`, `user[1]`, etc., instead of enabling `sqlite3.Row` for dictionary-like access to avoid altering too much of the data-handling logic.

- **Security over features**  
  Priority was given to hardening the system, not adding new user roles.


## What I'd Do With More Time

- Add unit & integration tests for each endpoint.
- Implement user authentication tokens (JWT).
- Validate email/password formats more strictly.
- Create a frontend dashboard or Swagger documentation.
- Add Schema Validation that Enforce request structure before processing.


## AI Tool Used: **ChatGPT by OpenAI**

**Purpose of Use:**

I used ChatGPT as a coding assistant to:
- Understand and fix security issues in the existing Flask codebase (e.g., password handling, SQL injection).
- Refactor functions and improve database handling logic using proper conn, cursor, commit() usage for SQLite.
- Get quick explanations for unfamiliar concepts (like check_password_hash, conn.commit(), or HTTP error status codes).
- Review and test edge cases in the API routes (GET, POST, DELETE).
- Suggest better practices while staying within project constraints.

> All changes made were reviewed, understood, and customized by me — ChatGPT acted as a mentor-like guide to speed up the learning and development process.

---



