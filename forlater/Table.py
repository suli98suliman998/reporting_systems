from sqlalchemy import Column, Integer, String

from forlater.Report import Report
from model import Base


class Table(Base):
    __tablename__ = 'table'
    id = Column(Integer, primary_key=True)
    column_titles = Column(String)
    row_titles = Column(String)
    table_content = Column(Integer, default=0)

    def fillRow(self, column_title, row_title, data):
        pass

    def buildTable(self, report: Report):
        pass

    def setColumnTitles(self, titles: [str]):
        self.column_titles = titles

    def setRowTitles(self, titles: [str]):
        self.row_titles = titles

    def setTableContent(self, content: [[str]]):
        self.table_content = content

    def getColumnTitles(self):
        return self.column_titles

    def getRowTitles(self):
        return self.row_titles

