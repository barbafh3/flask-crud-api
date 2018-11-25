from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import all model definitions from /api/db/models.py
from api.db.models import *

# Import declarative base from /api/db/base.py
from api.db.base import Base

engine = create_engine('postgres://postgres:@localhost:5432/', echo=True)

Base.metadata.create_all(engine)

# Starting DB session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# new_article = Article(title="Titulo 2", text="Texto 2")
# session.add(new_article)
# session.commit()

