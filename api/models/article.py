from sqlalchemy import Column, Integer, String

from api.app import ma
from api.db.base import Base

class Article(Base):

    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id','title','text')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)