import datetime

from Report_Manager.Table import Table
from Report_Manager.Type import Type
from User.User import User


class Form:
    def __init__(self, ID: int, fortType: Type, date: datetime, cycle: int, filledBy: int, dataToFill: Table):
        self.ID = ID
        self.type = fortType
        self.date = date
        self.cycle = cycle
        self.filledBy = filledBy
        self.dataToFill = dataToFill

    def submit(self):
        pass

    def validate_auth_to_submit(self):
        pass

    def reset(self):
        pass

    def setFilledBy(self, user_id):
        self.filledBy = user_id

    def set_table_data(self, table: Table):
        self.dataToFill = table

    def get_id(self):
        return self.ID

    def get_type(self):
        return self.type

    def get_date(self):
        return self.date

    def get_cycle(self):
        return self.cycle

    def get_filled_by(self):
        return self.filledBy
