from User.jobTitle import JobTitle


class User:
    def __init__(self, ID: int, name: str, username: str, jobTitle: JobTitle):
        self.__ID = ID
        self.__name = name
        self.__username = username
        self.__jobTitle = jobTitle

    def getID(self):
        return self.__ID

    def setName(self, name: str):
        self.__name = name

    def getName(self):
        return self.__name

    def setUsername(self, username: str):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setJobTitle(self, jobTitle: JobTitle):
        self.__jobTitle = jobTitle

    def getJobTitle(self):
        return self.__jobTitle

    # def login(self, username: str, password: str):
    #     # This is a simple example, in a real application you should check the credentials against a database
    #     if username == self.__username and password == self.__password:
    #         session["logged_in"] = True
    #         return True
    #     else:
    #         return False