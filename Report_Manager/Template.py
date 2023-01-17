

from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.dialects.postgresql import Any
from sqlalchemy.orm import relationship

from Report_Manager.Type import Type
from db import Base


class Template(Base):
    class Template(Base):
        __tablename__ = 'template'
        id = Column(Integer, primary_key=True)
        type = Column(Enum(Type))
        template_rows = relationship("TemplateRows", back_populates="template")


