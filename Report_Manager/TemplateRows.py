from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class TemplateRows(Base):
    __tablename__ = 'template_rows'
    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey('templates.id'))
    template = relationship("Template", back_populates="template_rows")


class TemplateRowsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TemplateRows
        include_relationships = True
        load_instance = True
