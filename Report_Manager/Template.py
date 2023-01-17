from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship
from Report_Manager.Type import Type
from db import Base


class Template(Base):
    __tablename__ = 'templates'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(Type))
    template_rows = relationship("TemplateRows", back_populates="template")

class TemplateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Template
        include_relationships = True
        load_instance = True
