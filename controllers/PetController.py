from flask import request

from services.PetService import PetService

service = PetService()


def store():
    return service.create_pet(request)


def show(pet_id):
    return service.get_pet(pet_id)


def update(pet_id):
    return service.update_pet(pet_id, request)


def delete(pet_id):
    return service.delete_pet(pet_id)


def list_pets():
    return service.list()
