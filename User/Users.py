from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, String, Enum, Integer
from sqlalchemy.dialects.postgresql import Any

from User.jobTitle import JobTitle
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
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


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        include_relationships = True
        load_instance = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)
