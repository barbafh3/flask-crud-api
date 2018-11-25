# Flask-CRUD-API

##    Root URL: http://localhost:5000

###    URL: http://localhost:5000/

###    Usage

#### Methods: GET

#### URL Params

This request requires no parameters

#### Success Response:

Should respond by showing this README.md file

#### Notes:

This is just an example README.md file for academical purposes

##    Articles

###    URL: http://localhost:5000/articles

Includes all methods associated with the model `Article`

#### Method: GET

#### URL Params

This request expects one of two possible request types: `listAll` or `findById`, and in case of the latter,
it should also include the id of the article to be returned

```json
{
"request-type": "listAll",
"id": "article_id"
}
```

#### Success Response:

The expected success response depends on request type:

* Request Type `listAll`: Should respond with a JSON formatted instances of all articles
* Request Type `findById`: Should respond with a JSON formatted instances of all articles

#### Error Response:

Should return an error in case of:

* When required parameters are missing
* When no articles for `listAll` 
* When no article with the id parameter was found.

