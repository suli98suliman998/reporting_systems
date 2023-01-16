from User.User import User
from User.jobTitle import JobTitle


class Labor(User):
    def __init__(self, ID: str, name: str, username: str, houseNu: int,
                 farmName: str):
        super().__init__(ID, name, username, jobTitle=JobTitle.LABOR)
        self.__houseNu = houseNu
        self.__farmName = farmName

    def setHouseNu(self, houseNu: int):
        self.__houseNu = houseNu

    def getHouseNu(self):
        return self.__houseNu

    def setFarmName(self, farmName: str):
        self.__farmName = farmName

    def getFarmName(self):
        return self.__farmName
