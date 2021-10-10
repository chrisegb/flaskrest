import logging

from flask import jsonify
from entities.models import User


class UserService:

    def __init__(self):
        self.logger = logging.getLogger('UserService')

    def create_user(self, request):
        if request:
            user = User()
            user.name = request.json['name']
            user.age = request.json['age']
            user.address = request.json['address']
            user.create()
            return jsonify(success=True)
        else:
            self.logger.error("The request is empty or null")
            return jsonify(success=False)

    def get_user(self, id_user):
        if id_user:
            user = User.query.get(id_user)
            if user:
                return jsonify(success=True, user=user.serialize)
            else:
                return jsonify(success=False, message='The user does not exists')

        else:
            self.logger.error("The user_id is null")
            return None

    def update_user(self, user_id, request):
        if user_id:
            user = User.query.get(user_id)
            user.name = request.json['name']
            user.age = request.json['age']
            user.address = request.json['address']
            User.update()
            return jsonify(success=True)
        else:
            self.logger.error("The user_id is null")
            return jsonify(success=False)

    def delete_user(self, user_id):
        if user_id:
            user = User.query.get(user_id)
            user.delete()
            return jsonify(success=True)
        else:
            self.logger.error("The user_id is null")
            return jsonify(success=False)

    @staticmethod
    def list():
        users = User.query.all()
        return jsonify(success=True, users=[user.serialize for user in users])
