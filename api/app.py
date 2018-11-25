import markdown
import os

from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

from api.config import *
from api.db.db import *

@app.route('/')
def readme():

    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        content = markdown_file.read()
        return markdown.markdown(content)