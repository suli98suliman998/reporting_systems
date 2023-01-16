import datetime
from Report_Manager.Table import Table
from Report_Manager.Type import Type
from User.User import User


class Report:
    def __init__(self, ID: str, title: str, reportType: Type, date: datetime, cycle: int, filledBy: User,
                 reviewedBy: User, userAccessList: [User], tableData: Table):
        self._ID = ID
        self._title = title
        self._type = reportType
        self._date = date
        self._cycle = cycle
        self._filledBy = filledBy
        self._reviewedBy = reviewedBy
        self._userAccessList = userAccessList
        self._tableData = Table

    def add_user_access(self, user: User):
        self._userAccessList.append(user)

    def remove_user_access(self, user: User):
        self._userAccessList.remove(user)