from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy import func

from api.models.article import *
from api.db.db import session

class Articles(Resource):

    def get(self):
        json_request = request.get_json()
        # Checking if the request content exists and if the request-type field exists
        if json_request:
            if json_request['request-type']:
                if (json_request['request-type'] == 'listAll'):
                    articles = session.query(Article).all()
                    response = articles_schema.dump(articles)
                    return jsonify(response.data)
                elif (json_request['request-type'] == 'findById'):
                    id = json_request['id']
                    article = session.query(Article) \
                                .filter(Article.id == id) \
                                .first()
                    if article:
                        response = article_schema.dump(article)
                        return jsonify(response.data)
                    else:
                        response = {
                            "message": "No article with the provided id was found"
                        }
                        return response, 404
                elif json_request['request-type'] == 'search':                    
                    if "title" in json_request['args'] and "text" in json_request['args']:
                        articles = session.query(Article) \
                                    .filter(func.lower(Article.title) == func.lower(json_request['args']['title'])) \
                                    .filter(func.lower(Article.text) == func.lower(json_request['args']['text'])) \
                                    .all()                        
                    elif "title" in json_request['args']:
                        articles = session.query(Article) \
                                    .filter(func.lower(Article.title) == func.lower(json_request['args']['title'])) \
                                    .all()    
                    elif "text" in json_request['args']:
                        articles = session.query(Article) \
                                    .filter(func.lower(Article.text) == func.lower(json_request['args']['text'])) \
                                    .all()    
                    else:
                        pass
                    if articles:
                        response = articles_schema.dump(articles)
                        return jsonify(response.data)
                    else:
                        response = {
                            "message": "No articles found"
                        }
                        return response, 404
                else:
                    response = {
                        "message": "Request-Type field is invalid"
                    }
                    return response, 400
            else:
                response = {
                    "message": "Request-Type field is required"
                }
                return response, 400
        else:
            response = {
                    "message": "This page requires a JSON formatted HTTP request and cannot be accessed directly"
                }
            return response, 400

    def post(self):
        json_request = request.get_json()
        # Checking if the request content exists and if the required fields text and title exist
        if json_request:
            if json_request['title'] and json_request['text']:
                try:
                    new_article = Article(title=json_request['title'], text=json_request['text'])
                    session.add(new_article)
                    session.commit()
                    response = article_schema.dump(new_article)
                    return jsonify(response.data)
                except Exception as e:
                    response = {
                        "message": "An internal error occurred when trying to save the article",
                        "errorLog": e 
                    }
                    return response, 500    
            else:
                response = {
                    "message": "Both title and text fields are required"
                }
                return response, 400
        else:
            response = {
                    "message": "This page requires a JSON formatted HTTP request and cannot be accessed directly"
                }
            return response, 400

    def put(self):
        json_request = request.get_json()
        # Checking if the request content exists and if the required fields text and title exist
        if json_request:            
            id = json_request['id']
            article = session.query(Article) \
                        .filter(Article.id == id) \
                        .first()
            if article:
                if json_request['title']:
                    article.title = json_request['title']
                else:
                    pass
                if json_request['text']:
                    article.text = json_request['text']
                else:
                    pass
                try:
                    session.add(article)
                    session.commit()
                    response = article_schema.dump(article)
                    return jsonify(response.data), 200
                except Exception as e:
                    return e, 500
            else:
                response = {
                    "message": "No article with the provided id was found"
                }
                return response, 404
   
        else:
            response = {
                    "message": "This page requires a JSON formatted HTTP request and cannot be accessed directly"
                }
            return response, 400

    def delete(self):
        json_request = request.get_json()
        # Checking if the request content exists and if the request-type field exists
        if json_request:
            if json_request['id']:
                id = json_request['id']
                try:
                    article = session.query(Article).filter(Article.id == id).first()
                    if article:
                        session.delete(article)
                        session.commit()
                        response = {
                            "message": "Article removed successfully"
                        }
                        return response
                    else:
                        response = {
                            "message": "No article with the provided id was found"
                        }
                        return response, 404
                except Exception as e:
                    response = {
                        "message": "An internal error occurred when trying to save the article",
                        "errorLog": e 
                    }
                    return response, 500 
            else:
                response = {
                    "message": "Id field is required"
                }
                return response, 400
        else:
            response = {
                    "message": "This page requires a JSON formatted HTTP request and cannot be accessed directly"
                }
            return response, 400