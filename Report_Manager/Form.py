from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from db import Base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Form(Base):
    __tablename__ = 'form'
    form_id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey('template.template_id'))
    filled_by = Column(Integer, ForeignKey('user.id'))
    farm_name = Column(String)
    barn_number = Column(Integer)
    metadata_id = Column(Integer, ForeignKey('metadata.metadata_id'))
    form_columns = relationship("FormColumns", back_populates="form", cascade="all, delete-orphan")


class FormSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Form
        include_relationships = True
        load_instance = True
