from flask import Blueprint

from controllers.PetController import store, show, update, delete, list_pets

pet_bp = Blueprint('pet_bp', __name__)

pet_bp.route('', methods=['POST'])(store)
pet_bp.route('', methods=['GET'])(list_pets)
pet_bp.route('/<int:pet_id>', methods=['GET'])(show)
pet_bp.route('/<int:pet_id>', methods=['PUT'])(update)
pet_bp.route('/<int:pet_id>', methods=['DELETE'])(delete)
