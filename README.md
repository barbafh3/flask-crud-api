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

#### Note:

All article requests require an Authorization header with a valid JWT security token:

* ``Authorization: JWT <Example-Token-Here>``

#### Method: GET

#### URL Params

This request expects one of these possible request types: `listAll`, `findById` and `search`

* Request Type `listAll`:
```json
{
    "request-type": "listAll"
}
```

* Request Type `findById`:
```json
{
    "request-type": "findById",
    "id": "article_id"
}
```
* Request Type `search`(neither title nor text is required here):
```json
{
    "request-type": "findById",
    "args": {
        "title": "title example", 
        "text": "text example"     
    }
}
```

#### Success Response:

The expected success response depends on request type:

* Request Type `listAll`: Should respond with JSON formatted list of all articles
* Request Type `findById`: Should respond with a JSON formatted instance of article
* Request Type `search`: Should respond with a JSON formatted list of articles as search result

#### Error Response:

Should return an error in case of:

* When required parameters are missing
* When no articles for `listAll` 
* When no article with the id parameter was found.

