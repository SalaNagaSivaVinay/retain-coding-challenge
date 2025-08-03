from db import get_db_connection
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                   (username, email, hash_password(password)))
    conn.commit()
    conn.close()

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    user = cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return user

def get_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    user = cursor.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    return user

def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    users = cursor.execute("SELECT * FROM users").fetchall()
    conn.close()
    return users

def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

def update_user(user_id, username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?",
        (username, email, hash_password(password), user_id)
    )
    conn.commit()
    conn.close()

def search_users_by_name(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    users = cursor.execute(
        "SELECT * FROM users WHERE username LIKE ?", (f'%{name}%',)
    ).fetchall()
    conn.close()
    return users

def login_user(username, password):
    user = get_user_by_username(username)
    if user and user['password'] == hash_password(password):
        return user
    return None
