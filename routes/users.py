# routes/users.py

from flask import Blueprint, request, jsonify
from services.user_service import get_all_users, get_user_by_id
from utils.validators import validate_user_data

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users), 200

@users_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404
