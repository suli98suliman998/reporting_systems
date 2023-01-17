from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# create an engine and a session factory
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()