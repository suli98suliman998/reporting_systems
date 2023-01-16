import datetime
from Report_Manager.Table import Table
from Report_Manager.Type import Type


class Report:
    def __init__(self, ID: int, title: str, reportType: Type, date: datetime, cycle: int, filledBy: int,
                 reviewedBy: int, userAccessList: [int], tableData: Table):
        self._ID = ID
        self._title = title
        self._type = reportType
        self._date = date
        self._cycle = cycle
        self._filledBy = filledBy
        self._reviewedBy = reviewedBy
        self._userAccessList = userAccessList
        self._tableData = tableData

    def set_reviewedBy(self, reviewedBy: int):
        self._reviewedBy = reviewedBy

    def validate_authority_to_review(self, user_id):
        if user_id in self._userAccessList:
            return True
        else:
            return False

    def set_access_list(self, users: [int]):
        self._userAccessList = users

    def set_table_data(self, table: Table):
        self._tableData = table

    def get_ID(self):
        return self._ID

    def get_title(self):
        return self._title

    def get_type(self):
        return self._type

    def get_date(self):
        return self._date

    def get_cycle(self):
        return self._cycle

    def get_reviewed_by(self):
        return self._reviewedBy

    def get_user_access_list(self):
        return self._userAccessList

    def get_table_data(self):
        return self._tableData

