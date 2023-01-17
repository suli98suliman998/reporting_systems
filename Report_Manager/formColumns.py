from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from db import Base


class FormColumns(Base):
    __tablename__ = 'form_columns'
    form_id = Column(Integer, ForeignKey('form.form_id'), primary_key=True)
    column_title = Column(String, primary_key=True)
    form = relationship("Form", back_populates="form_columns")


class FormColumnsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = FormColumns
        include_relationships = True
        load_instance = True
