class Student:
    def __init__(self, discordId: int):
        self.names = None
        self.lastNames = None
        self.collegeId = None
        self.email = None
        self.phoneNum = None
        self.discordId = discordId

    # Getters and setters

    def getNames(self) -> str:
        output = None

        if self.names is not None:
            output = self.names
        else:
            output = 'unknown'

        return output

    def getLastNames(self) -> str:
        output = None

        if self.lastNames is not None:
            output = self.lastNames
        else:
            output = 'unknown'

        return output

    def getCollegeId(self) -> int:
        output = None

        if self.collegeId is not None:
            output = self.collegeId
        else:
            output = -1

        return output

    def getEmail(self) -> str:
        output = None

        if self.email is not None:
            output = self.email
        else:
            output = 'unknown'

        return output

    def getPhoneNumber(self) -> int:
        output = None

        if self.phoneNum is not None:
            output = self.phoneNum
        else:
            output = -1

        return output

    def getDiscordId(self) -> int:
        return self.discordId

    def setNames(self, names: str):
        self.names = names

    def setLastNames(self, lastNames: str):
        self.lastNames = lastNames

    def setCollegeId(self, id: int):
        self.collegeId = id

    def setEmail(self, email: str):
        self.email = email

    def setPhoneNumber(self, phoneNum: int):
        self.phoneNum = phoneNum

    def setDiscordId(self, id: int):
        self.discordId = id

    # Printing data

    def toString(self) -> str:
        return f'👤 Names: {self.getNames()}, Last Names: {self.getLastNames()}, Id: {self.getCollegeId()},\nEmail: {self.getEmail()}, Phone number: {self.getPhoneNumber()}'

    def toCSV(self) -> str:
        return f'{self.getNames()},{self.getLastNames()},{self.getCollegeId()},{self.getEmail()},{self.getPhoneNumber()}'

    # Dictionary

    def toDict(self) -> dict:
        return {
            "Names" : self.names,
            "LastNames" : self.lastNames,
            "CollegeId" : self.collegeId,
            "Email" : self.email,
            "PhoneNumber" : self.phoneNum,
            "DiscordId" : self.discordId
        }
