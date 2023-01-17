from sqlalchemy import Integer, Column, String, ForeignKey

from db import Base


class SubmittedData(Base):
    __tablename__ = 'submitted_data'
    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey('template.id'))
    row_title = Column(String)
    report_id = Column(Integer, ForeignKey('report.id'))
    column_title = Column(String)
    data = Column(String)