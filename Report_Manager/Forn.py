import datetime

from Report_Manager.Table import Table
from Report_Manager.Type import Type
from User.User import User


class Form:
    def __init__(self, ID:str, fortType:Type, date:datetime, cycle:int, filledBy:User):
        self.ID = ID
        self.type = fortType
        self.date = date
        self.cycle = cycle
        self.filledBy = filledBy
        self.dataToFill = Table()