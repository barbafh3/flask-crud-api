from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import all model definitions from /api/db/models.py
import api.models.article
import api.models.user

# Import declarative base from /api/db/base.py
from api.db.base import Base

engine = create_engine('postgres://postgres:@localhost:5432/', echo=True)

Base.metadata.create_all(engine)

# Starting DB session
DBSession = sessionmaker(bind=engine)
session = DBSession()


