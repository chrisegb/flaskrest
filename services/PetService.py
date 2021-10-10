import logging

from flask import jsonify
from entities.models import Pet
from entities.models import User


class PetService:

    def __init__(self):
        self.logger = logging.getLogger('PetService')

    def create_pet(self, request):
        if request:
            pet = Pet()
            pet.name = request.json['name']
            pet.type = request.json['type']
            pet.age = request.json['age']
            pet.user_id = request.json['user_id']
            pet.create()
            return jsonify(success=True)
        else:
            self.logger.error("The request is empty or null")
            return jsonify(success=False)

    def get_pet(self, pet_id):
        if pet_id:
            pet = Pet.query.get(pet_id)
            if pet:
                return jsonify(success=True, pet=pet.serialize)
            else:
                return jsonify(success=False, message='The pet does not exists')

        else:
            self.logger.error("The pet_id is null")
            return None
        pass

    def update_pet(self, pet_id, request):
        if pet_id:
            pet = Pet.query.get(pet_id)
            pet.name = request.json['name']
            pet.age = request.json['age']
            pet.type = request.json['type']
            pet.user_id = request.json['user_id']
            Pet.update()
            return jsonify(success=True)
        else:
            self.logger.error("The pet_id is null")
            return jsonify(success=False)

    def delete_pet(self, pet_id):
        if pet_id:
            pet = Pet.query.get(pet_id)
            pet.delete()
            return jsonify(success=True)
        else:
            self.logger.error("The pet_id is null")
            return jsonify(success=False)

    @staticmethod
    def list():
        pets = Pet.query.all()
        return jsonify(success=True, pets=[pet.serialize for pet in pets])
