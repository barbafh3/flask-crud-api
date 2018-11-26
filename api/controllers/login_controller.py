from flask import request, jsonify

from api.models.user import User
from api.db.db import session
from api.app import bcrypt

def verify(username, password):
    if not (username and password):
        return False
    user = session.query(User) \
            .filter(User.username == username) \
            .first()
    # hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
    if user and bcrypt.check_password_hash(user.password, password):
        return User(id = user.id)
    # if USER_DATA.get(username) == password:
    #     return User(id=123)


def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}