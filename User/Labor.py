from sqlalchemy import Column, String, Integer
from User.User import User
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


