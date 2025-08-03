# services/user_service.py

from db.database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

# Get all users
def get_all_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return [dict(user) for user in users]

# Get user by ID
def get_user_by_id(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    return dict(user) if user else None

# Create a new user
def create_user(username, email, password):
    conn = get_db_connection()
    existing_user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    if existing_user:
        conn.close()
        return {"message": "User with this email already exists"}, 400

    hashed_password = generate_password_hash(password)
    conn.execute(
        'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
        (username, email, hashed_password)
    )
    conn.commit()
    conn.close()
    return {"message": "User created successfully"}, 201

# Update user
def update_user(user_id, data):
    conn = get_db_connection()
    conn.execute(
        'UPDATE users SET username = ?, email = ? WHERE id = ?',
        (data.get('username'), data.get('email'), user_id)
    )
    conn.commit()
    conn.close()
    return "User updated successfully"

# Delete user
def delete_user(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return "User deleted successfully"

# Search users by name
def search_users_by_name(name):
    conn = get_db_connection()
    users = conn.execute(
        'SELECT * FROM users WHERE username LIKE ?', (f'%{name}%',)
    ).fetchall()
    conn.close()
    return [dict(user) for user in users]

# Login
def login_user(data):
    email = data.get("email")
    password = data.get("password")

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    conn.close()

    if user and check_password_hash(user["password"], password):
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid email or password"}, 401
