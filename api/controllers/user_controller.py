from flask_restful import Resource

from api.app import bcrypt

class Users(Resource):

    def get(self):
        # get users by ID, search fields or list all users
        pass

    def post(self):
        # save new user
        pass

    def put(self):
        # update user
        pass
    
    def delete(self):
        # delete user
        pass