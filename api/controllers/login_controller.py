from flask import request, jsonify

from api.db.db import session

def verify(username, password):
    if not (username and password):
        return False
    # check for real user data
    # if USER_DATA.get(username) == password:
    #     return User(id=123)


def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}