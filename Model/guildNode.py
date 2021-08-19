from Model.subject import *

class GuildNode:
    def __init__(self, guildId: int):
        self.guildId = guildId
        self.subjects = []

    # Getters and setters

    def getGuildId(self) -> int:
        return self.guildId

    def setGuildId(self, guildId: int):
        self.getGuildId = guildId

    # Subjects management

    def __verifySubjectExistence(self, subjectName: str) -> bool:
        exists = False

        for subject in self.subjects:
            if subject.getName() == subjectName:
                exists = True
                break

        return exists

    def addSubject(self, subjectName: str) -> bool:
        flag = True

        try:
            if not self.__verifySubjectExistence(subjectName):
                s = Subject(subjectName)
                self.subjects.append(s)
            else:
                flag= False
        except:
            flag = False
        
        return flag

    def removeSubject(self, subjectName: str) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.getName() == subjectName:
                self.subjects.remove(subject)
                flag = True
                break

        return flag

    # Students management

    def addStudent(self, subjectName: str, discordId: int) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.getName() == subjectName:
                flag = subject.addStudent(discordId)
                break

        return flag

    def removeStudent(self, subjectName: str, discordId: int) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.getName() == subjectName:
                flag = subject.removeStudent(discordId)
                break

        return flag

    def editStudentNames(self, names: str, discordId: int) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.editStudentNames(names, discordId):
                flag = True

        return flag

    def editStudentLastNames(self, lastNames: str, discordId: int) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.editStudentLastNames(lastNames, discordId):
                flag = True

        return flag

    def editStudentCollegeId(self, collegeId: int, discordId: int) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.editStudentCollegeId(collegeId, discordId):
                flag = True

        return flag

    def editStudentEmail(self, email: str, discordId: int) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.editStudentEmail(email, discordId):
                flag = True

        return flag

    def editStudentPhoneNumber(self, phoneNum: int, discordId: int) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.editStudentPhoneNumber(phoneNum, discordId):
                flag = True

        return flag

    # Links management

    def addLink(self, subjectName: str, name: str, url: str) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.getName() == subjectName:
                flag = subject.addLink(name, url)
                break

        return flag

    def removeLink(self, subjectName: str, index: int) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.getName() == subjectName:
                flag = subject.removeLink(index)
                break

        return flag

    # Notes management

    def addNote(self, subjectName: str, name: str, text: str) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.getName() == subjectName:
                flag = subject.addNote(name, text)
                break

        return flag

    def removeNote(self, subjectName: str, index: int) -> bool:
        flag = False

        for subject in self.subjects:
            if subject.getName() == subjectName:
                flag = subject.removeNote(index)
                break

        return flag

    # Printing data

    def getAllStudents(self) -> str:
        output = ''

        for subject in self.subjects:
            output = output + subject.getStudents() + '\n'

        if output != '': output = output[:-1]

        return output

    def getStudentsFromSubject(self, subjectName: str) -> str:
        output = ''

        for subject in self.subjects:
            if subject.getName() == subjectName:
                output = subject.getStudents()
                break

        return output

    def getStudentFromSubject(self, subjectName: str, discordId: int) -> str:
        output = ''

        for subject in self.subjects:
            if subject.getName() == subjectName:
                output = subject.getStudent(discordId)
                break

        return output

    def getLinksFromSubject(self, subjectName: str) -> str:
        output = ''

        for subject in self.subjects:
            if subject.getName() == subjectName:
                output = subject.getLinks()
                break

        return output

    def getNotesFromSubject(self, subjectName: str) -> str:
        output = ''

        for subject in self.subjects:
            if subject.getName() == subjectName:
                output = subject.getNotes()
                break

        return output

    # Dictionary

    def toDict(self) -> dict:
        listDict = []

        for subject in self.subjects:
            listDict.append(subject.toDict())

        return {
            "GuildId" : self.guildId,
            "Subjects" : listDict
        }
