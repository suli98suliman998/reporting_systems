from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
# from sqlalchemy.testing import db

# from app import app

Base = declarative_base()

engine = create_engine('sqlite:///database.db')

# Create the tables in the database
Base.metadata.create_all(bind=engine)
