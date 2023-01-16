import datetime

from Report_Manager.Form import Form
from Report_Manager.Report import Report
from Report_Manager.Type import Type


class ReportingServices:
    def __init__(self):
        self.__forms = []
        self.__reports = []

    def getForm(self, formType: Type):
        pass

    def submitForm(self, form: Form):
        pass

    def getReportByID(self, ID: str):
        pass

    def getReportByDate(self, date: datetime):
        pass

    def getReportByType(self, reportType: Type):
        pass

    def setReportReviewed(self, report: Report, user_id: str):
        pass
