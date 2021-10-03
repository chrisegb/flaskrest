from flask_sqlalchemy import SQLAlchemy

user_db = SQLAlchemy()


class User(user_db.Model):
    __tablename__ = 'users'

    id = user_db.Column(user_db.Integer, primary_key=True)
    name = user_db.Column(user_db.String)
    age = user_db.Column(user_db.String(120))
    address = user_db.Column(user_db.String(120))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'address': self.address
        }
