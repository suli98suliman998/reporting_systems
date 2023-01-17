from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Integer, Column, String, ForeignKey, PrimaryKeyConstraint

from db import Base


class SubmittedData(Base):
    __tablename__ = 'submitted_data'
    template_id = Column(Integer, primary_key=True)
    row_title = Column(String, primary_key=True)
    form_id = Column(Integer, primary_key=True)
    column_title = Column(String, primary_key=True)
    data = Column(String)
    __table_args__ = (PrimaryKeyConstraint('template_id', 'row_title', 'form_id', 'column_title'),)


class SubmittedDataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SubmittedData
        include_relationships = True
        load_instance = True



