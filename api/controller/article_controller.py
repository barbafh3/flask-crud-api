from flask import request, jsonify
from flask_restful import Resource

from api.db.models import *
from api.db.db import session

class ArticleRead(Resource):

    def get(self):
        json_request = request.get_json()
        if (json_request['request-type'] == 'listAll'):
            articles = session.query(Article).all()
            response = articles_schema.dump(articles)
            return jsonify(response.data)
        elif (json_request['request-type'] == 'findById'):
            id = json_request['id']
            article = session.query(Article).filter(Article.id == id).one()
            response = article_schema.dump(article)
            return jsonify(response.data)
        else:
            pass

    def post(self):
        pass        

    def put(self):
        pass

    def delete(self):
        pass