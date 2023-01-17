from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class ReportColumn(Base):
    __tablename__ = 'report_column'
    id = Column(Integer, primary_key=True)
    report_id = Column(Integer, ForeignKey('report.id'))
    column_title = Column(String)
    report = relationship("Report", back_populates="report_column")
