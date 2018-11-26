import markdown
import os

from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_jwt import JWT, jwt_required
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-duper-secret'
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

from api.controllers.login_controller import verify, identity

jwt = JWT(app, verify, identity)

import api.config 
import api.db.db

@app.route('/')
def readme():

    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        content = markdown_file.read()
        return markdown.markdown(content)