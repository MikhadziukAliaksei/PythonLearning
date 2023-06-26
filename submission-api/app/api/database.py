from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .db import Base

engine = create_engine('postgresql://postgres:postgrespw@localhost:55000/test')
Session = sessionmaker(bind=engine)


Base.metadata.create_all(engine)
