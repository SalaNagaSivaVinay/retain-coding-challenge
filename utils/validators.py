# utils/validators.py

def validate_user_data(data):
    if not data.get("name") or not data.get("email") or not data.get("password"):
        return False, "Name, email, and password are required."
    return True, ""
