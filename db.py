from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create an engine and a session factory
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)

