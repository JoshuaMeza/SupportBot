from Model.student import *
from Model.link import *
from Model.note import *

class Subject:
    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.linkIndex = 0
        self.links = []
        self.noteIndex = 0
        self.notes = []

    # Getters and setters
    
    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

    def getNextLinkIndex(self) -> int:
        self.linkIndex = self.linkIndex + 1
        return self.linkIndex - 1

    def getNextNoteIndex(self) -> int:
        self.noteIndex = self.noteIndex + 1
        return self.noteIndex - 1

    # Students management

    def __verifyStudentExistence(self, discordId: int) -> bool:
        exists = False

        for student in self.students:
            if student.getDiscordId() == discordId:
                exists = True
                break

        return exists

    def addStudent(self, discordId: int) -> bool:
        flag = True

        try:
            if not self.__verifyStudentExistence(discordId):
                s = Student(discordId)
                self.students.append(s)
            else:
                flag = False
        except:
            flag = False
        
        return flag

    def removeStudent(self, discordId: int) -> bool:
        flag = False

        for student in self.students:
            if student.getDiscordId() == discordId:
                self.students.remove(student)
                flag = True
                break

        return flag

    def editStudentNames(self, names: str, discordId: int) -> bool:
        flag = False

        for student in self.students:
            if student.getDiscordId() == discordId:
                student.setNames(names)
                flag = True
                break

        return flag

    def editStudentLastNames(self, lastNames: str, discordId: int) -> bool:
        flag = False

        for student in self.students:
            if student.getDiscordId() == discordId:
                student.setLastNames(lastNames)
                flag = True
                break

        return flag

    def editStudentCollegeId(self, collegeId: int, discordId: int) -> bool:
        flag = False

        for student in self.students:
            if student.getDiscordId() == discordId:
                student.setCollegeId(collegeId)
                flag = True
                break

        return flag

    def editStudentEmail(self, email: str, discordId: int) -> bool:
        flag = False

        for student in self.students:
            if student.getDiscordId() == discordId:
                student.setEmail(email)
                flag = True
                break

        return flag

    def editStudentPhoneNumber(self, phoneNum: int, discordId: int) -> bool:
        flag = False

        for student in self.students:
            if student.getDiscordId() == discordId:
                student.setPhoneNumber(phoneNum)
                flag = True
                break

        return flag

    # Links management

    def addLink(self, name: str, url: str) -> bool:
        flag = True

        try:
            l = Link(self.getNextLinkIndex(), name, url)
            self.links.append(l)
        except:
            flag = False

        return flag

    def removeLink(self, index: int) -> bool:
        flag = False

        for link in self.links:
            if link.getIndex() == index:
                self.links.remove(link)
                flag = True
                break

        return flag

    # Notes management

    def addNote(self, name: str, text: str) -> bool:
        flag = True

        try:
            n = Note(self.getNextNoteIndex(), name, text)
            self.notes.append(n)
        except:
            flag = False

        return flag

    def removeNote(self, index: int) -> bool:
        flag = False

        for note in self.notes:
            if note.getIndex() == index:
                self.notes.remove(note)
                flag = True
                break

        return flag

    # Printing data

    def getStudents(self) -> str:
        output = ''

        for student in self.students:
            output = output + student.toString() + '\n'

        if output != '': output = output[:-1]

        return output

    def getStudent(self, discordId: int) -> str:
        output = ''

        for student in self.students:
            if student.getDiscordId() == discordId:
                output = student.toString()
                break

        return output

    def getLinks(self) -> str:
        output = ''

        for link in self.links:
            output = output + link.toString() + '\n'

        if output != '': output = output[:-1]

        return output

    def getNotes(self) -> str:
        output = ''

        for note in self.notes:
            output = output + note.toString() + '\n'

        if output != '': output = output[:-1]

        return output

    # Dictionary

    def toDict(self) -> dict:
        studentDict = []
        linkDict = []
        noteDict = []

        for student in self.students:
            studentDict.append(student.toDict())

        for link in self.links:
            linkDict.append(link.toDict())

        for note in self.notes:
            noteDict.append(note.toDict())

        return {
            "SubjectName" : self.name,
            "Members" : studentDict,
            "Links" : linkDict,
            "Notes" : noteDict
        }
    