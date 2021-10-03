import logging

from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from entities.User import User


class UserService:

    def __init__(self):
        self.dao = SQLAlchemy()
        self.logger = logging.getLogger('UserService')

    def create_user(self, request):
        if request:
            user = User()
            user.name = request.json['name']
            user.age = request.json['age']
            user.address = request.json['address']
            self.dao.session.add(user)
            self.dao.session.commit()
            return jsonify(success=True)
        else:
            self.logger.error("The request is empty or null")
            return jsonify(success=False)

    def get_user(self, id_user):
        if id_user:
            user = self.dao.session.query(User).get(id_user)
            return jsonify(user.serialize)
        else:
            self.logger.error("The user_id is null")
            return None

    def update_user(self, user_id, request):
        if user_id:
            user = self.dao.session.query(User).get(user_id)
            user.name = request.json['name']
            user.age = request.json['age']
            user.address = request.json['address']
            self.dao.session.commit()
            return jsonify(success=True)
        else:
            self.logger.error("The user_id is null")
            return jsonify(success=False)

    def delete_user(self, user_id):
        if user_id:
            self.dao.session.query(User).filter(User.id == user_id).delete()
            self.dao.session.commit()
            return jsonify(success=True)
        else:
            self.logger.error("The user_id is null")
            return jsonify(success=False)

    def list(self):
        users = self.dao.session.query(User).all()
        return jsonify([user.serialize for user in users])
