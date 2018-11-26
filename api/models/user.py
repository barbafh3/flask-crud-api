from sqlalchemy import Column, Integer, String

from api.app import ma
from api.db.base import Base

class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','title','text')

user_schema = UserSchema()
users_schema = UserSchema(many=True)