from flask import Blueprint

from controllers.UserController import store, show, update, delete, list_users, list_user_pets

user_bp = Blueprint('user_bp', __name__)

user_bp.route('', methods=['POST'])(store)
user_bp.route('', methods=['GET'])(list_users)
user_bp.route('/<int:user_id>', methods=['GET'])(show)
user_bp.route('/<int:user_id>', methods=['PUT'])(update)
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete)
user_bp.route('/<int:user_id>/pets', methods=['GET'])(list_user_pets)
