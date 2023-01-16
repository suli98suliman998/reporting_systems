from sqlalchemy import Column, String, Enum, Integer
from sqlalchemy.dialects.postgresql import Any

from User.jobTitle import JobTitle
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    jobTitle = Column(Enum(JobTitle))

    def __init__(self, name, username, jobTitle, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.name = name
        self.username = username
        self.jobTitle = jobTitle


