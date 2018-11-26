from flask import Flask
from flask_restful import Api, Resource

from api.app import app

# Import all controllers to be set into routes
from api.controllers.article_controller import Articles

# Set up the api to make the routes
api = Api(app)

# Using the api to make routes
api.add_resource(Articles, '/articles')