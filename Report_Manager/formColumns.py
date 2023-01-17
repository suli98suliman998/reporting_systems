from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from db import Base


class FormColumns(Base):
    __tablename__ = 'form_columns'
    id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey('form.id'))
    column_title = Column(String)
    form = relationship("Form", back_populates="form_columns")
