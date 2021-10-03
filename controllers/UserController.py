from flask import request

from services.UserService import UserService

service = UserService()


def store():
    return service.create_user(request)


def show(user_id):
    return service.get_user(user_id)


def update(user_id):
    return service.update_user(user_id, request)


def delete(user_id):
    return service.delete_user(user_id)


def list_users():
    return service.list()
