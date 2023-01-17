from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, String, Integer
from User.Users import User
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Labor(User):
    __tablename__ = 'labors'

    id = Column(Integer, primary_key=True)
    houseNu = Column(Integer)
    farmName = Column(String)

    def __init__(self, name, username, jobTitle, houseNu, farmName):
        super().__init__(name, username, jobTitle)
        self.houseNu = houseNu
        self.farmName = farmName

class LaborSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Labor
        include_relationships = True
        load_instance = True
