import datetime


from sqlalchemy import Column, Enum, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from Report_Manager.Table import Table
from Report_Manager.Type import Type
from User.User import User
from db import Base


class Form(Base):
    __tablename__ = 'form'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(Type))
    datetime = Column(DateTime, default=datetime.datetime.utcnow)
    cycle = Column(Integer)
    filled_by = Column(Integer, ForeignKey('user.id'))
    data_to_fill = Column(Integer, ForeignKey('table.id'))
    form_columns = relationship("FormColumns", back_populates="form")
