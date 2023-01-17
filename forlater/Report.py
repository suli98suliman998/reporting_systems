import datetime

from sqlalchemy import Column, Integer, ForeignKey, Enum, String, DateTime
from sqlalchemy.dialects.postgresql import Any
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from forlater.Table import Table
from Report_Manager.Type import Type

Base = declarative_base()


class Report(Base):
    __tablename__ = 'report'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    type = Column(Enum(Type))
    date = Column(DateTime, default=datetime.datetime.utcnow)
    cycle = Column(Integer)
    reviewed_by = Column(Integer, ForeignKey('user.id'))
    user_access = Column(String)
    table_data = Column(Integer, ForeignKey('table.id'))
    report_column = relationship("ReportColumn", back_populates="report")
    generated_report = relationship("GeneratedReport", back_populates="report")

    def __init__(self, title: str, type: Type, cycle: int, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.title = title
        self.type = type
        self.cycle = cycle

    def setReviewedBy(self, user_id: int):
        self.reviewed_by = user_id

    def setTableData(self, table: Table):
        self.table_data = table

    def validateAccessToReview(self):
        pass

    def getID(self):
        return self.id

    def getTitle(self):
        return self.title

    def getType(self):
        return self.type

    def getCycle(self):
        return self.cycle

    def getReviewdBy(self):
        return self.reviewed_by

    def getTableData(self):
        return self.table_data

    def getUserAccessList(self):
        return self.user_access