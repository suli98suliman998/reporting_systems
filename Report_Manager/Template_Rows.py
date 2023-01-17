from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class TemplateRows(Base):
    __tablename__ = 'template_rows'
    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey('template.id'))
    row_title = Column(String)
    template = relationship("Template", back_populates="template_rows")