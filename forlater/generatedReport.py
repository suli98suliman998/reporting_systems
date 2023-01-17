from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from model import Base


class GeneratedReport(Base):
    __tablename__ = 'generated_report'
    id = Column(Integer, primary_key=True)
    report_id = Column(Integer, ForeignKey('report.id'))
    template_id = Column(Integer, ForeignKey('template.id'))
    row_title = Column(String)
    column_title = Column(String)
    data = Column(String)
    report = relationship("Report", back_populates="generated_report")