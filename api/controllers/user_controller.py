from flask import request, jsonify
from flask_restful import Resource

from api.app import bcrypt
from api.models.user import User, user_schema, users_schema
from api.db.db import session

class Users(Resource):

    def get(self):
        users = session.query(User).all()
        response = users_schema.dump(users)
        return jsonify(response.data)

    def post(self):
        json_request = request.get_json()
        if json_request:
            if 'username' in json_request and 'password' in json_request:
                hash_password = bcrypt.generate_password_hash(json_request['password']).decode('utf-8')
                new_user = User(username = json_request['username'], password = hash_password)
                session.add(new_user)
                session.commit()
                response = user_schema.dump(new_user)
                return response.data, 201
            else:
                return 400
        else:
            return 400
        return 400

    def put(self):
        # update user
        pass
    
    def delete(self):
        # delete user
        pass