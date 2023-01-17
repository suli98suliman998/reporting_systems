import datetime

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import String, Column, DateTime, Integer

from db import Base


class Metadata(Base):
    __tablename__ = 'metadata'
    metadata_id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    time = Column(String)
    title = Column(String)


class MetadataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Metadata
        include_relationships = True
        load_instance = True

Metadata_Schema = MetadataSchema()
Metadatas_Schema = MetadataSchema(many=True)
