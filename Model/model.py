import discord
from Model.fileHandler import *
from Model.guildNode import *

class Model:
    def __init__(self):
        self.errColor = discord.Colour.from_rgb(225, 7, 0)
        self.defColor = discord.Colour.from_rgb(0, 239, 134)
        self.prefix = '!'
        self.fileName = 'memory.json'
        self.noInfoAnswer = 'There\'s no information related'
        self.lockRoleName = 'BotManager'
        self.guilds = []

        self.__buildGuilds()

    # Getters and setters

    def getPrefix(self) -> str:
        return self.prefix

    def getErrorColor(self) -> discord.Colour:
        return self.errColor

    def getDefaultColor(self) -> discord.Colour:
        return self.defColor

    def getLockRoleName(self) -> str:
        return self.lockRoleName

    # File management

    def __readData(self) -> dict:
        fileHandler = FileHandler()
        return fileHandler.readJSON(self.fileName)

    def __writeData(self, info: dict) -> bool:
        fileHandler = FileHandler()
        return fileHandler.writeJSON(self.fileName, info)

    def __updatePersistentData(self) -> bool:
        listDict = []

        for guild in self.guilds:
            listDict.append(guild.toDict())

        return self.__writeData({"Guilds" : listDict})

    # Guilds management

    def __buildGuilds(self):
        info = self.__readData()
        index = 0

        try:
            for guild in info['Guilds']:
                # Move through all guilds

                if self.addGuild(guild['GuildId'], False):
                    # Avoid duplicates

                    for subject in guild['Subjects']:
                        # Move through all subjects
                        subjectName = subject['SubjectName']
                        
                        if self.guilds[index].addSubject(subjectName):
                            # Avoid duplicates
                            # Start adding the subject data ¬

                            for student in subject['Members']:
                                # Move through all students
                                discordId = student['DiscordId']

                                if self.guilds[index].addStudent(subjectName, discordId):
                                    #Adding aditional information of students

                                    if student['Names'] is not None:
                                        self.guilds[index].editStudentNames(student['Names'], discordId)

                                    if student['LastNames'] is not None:
                                        self.guilds[index].editStudentLastNames(student['LastNames'], discordId)

                                    if student['CollegeId'] is not None:
                                        self.guilds[index].editStudentCollegeId(student['CollegeId'], discordId)

                                    if student['Email'] is not None:
                                        self.guilds[index].editStudentEmail(student['Email'], discordId)

                                    if student['PhoneNumber'] is not None:
                                        self.guilds[index].editStudentPhoneNumber(student['PhoneNumber'], discordId)

                            for link in subject['Links']:
                                # Move through all links
                                self.guilds[index].addLink(subjectName, link['Name'], link['URL'])

                            for note in subject['Notes']:
                                # Move through all notes
                                self.guilds[index].addNote(subjectName, note['Name'], note['Text'])

                    index += 1
        except KeyError:
            print('Memory loading problem!')

    def __verifyGuildExistence(self, guildId) -> bool:
        exists = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                exists = True
                break

        return exists

    def addGuild(self, guildId: int, overwrite = True) -> bool:
        flag = True

        try:
            if not self.__verifyGuildExistence(guildId):
                g = GuildNode(guildId)
                self.guilds.append(g)
            else:
                flag = False
        except:
            flag = False

        if flag and overwrite:
            self.__updatePersistentData()

        return flag

    def removeGuild(self, guildId: int) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                self.guilds.remove(guild)
                flag = True
                break

        if flag:
            self.__updatePersistentData()

        return flag

    # Subjects management

    def addSubjectToGuild(self, guildId: int, subjectName: str) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.addSubject(subjectName)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    def removeSubjectOfGuild(self, guildId: int, subjectName: str) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.removeSubject(subjectName)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    def containsSubject(self, guildId: int, subjectName: str) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.containsSubject(subjectName)
                break

        return flag


    # Students management

    def addStudentToSubjectFromGuild(self, guildId: int, subjectName: str, discordId: int) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.addStudent(subjectName, discordId)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    def removeStudentOfSubjectFromGuild(self, guildId: int, subjectName: str, discordId: int) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.removeStudent(subjectName, discordId)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    def editStudentNamesFromGuild(self, guildId: int, names: str, discordId: int) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.editStudentNames(names, discordId)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    def editStudentLastNamesFromGuild(self, guildId: int, lastNames: str, discordId: int) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.editStudentLastNames(lastNames, discordId)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    def editStudentCollegeIdFromGuild(self, guildId: int, collegeId: int, discordId: int) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.editStudentCollegeId(collegeId, discordId)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    def editStudentEmailFromGuild(self, guildId: int, email: str, discordId: int) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.editStudentEmail(email, discordId)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    def editStudentPhoneNumberFromGuild(self, guildId: int, phoneNum: int, discordId: int) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.editStudentPhoneNumber(phoneNum, discordId)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    # Links management

    def addLinkToSubjectFromGuild(self, guildId: int, subjectName: str, name: str, url: str) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.addLink(subjectName, name, url)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    def removeLinkOfSubjectFromGuild(self, guildId: int, subjectName: str, index: int) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.removeLink(subjectName, index)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    # Notes management

    def addNoteToSubjectFromGuild(self, guildId: int, subjectName: str, name: str, text: str) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.addNote(subjectName, name, text)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    def removeNoteOfSubjectFromGuild(self, guildId: int, subjectName: str, index: int) -> bool:
        flag = False

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                flag = guild.removeNote(subjectName, index)
                break

        if flag:
            self.__updatePersistentData()

        return flag

    # Printing data

    def getStudentsFromSubject(self, guildId: int, subjectName: str) -> str:
        output = ''

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                output = guild.getStudentsFromSubject(subjectName)
                break

        if output == '':
            output = self.noInfoAnswer

        return output

    def getStudentFromSubject(self, guildId: int, subjectName: str, discordId: int, CSV: bool) -> str:
        output = ''

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                output = guild.getStudentFromSubject(subjectName, discordId, CSV)
                break

        if output == '':
            output = self.noInfoAnswer

        return output

    def getLinksFromSubject(self, guildId: int, subjectName: str) -> str:
        output = ''

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                output = guild.getLinksFromSubject(subjectName)
                break

        if output == '':
            output = self.noInfoAnswer

        return output

    def getNotesFromSubject(self, guildId: int, subjectName: str) -> str:
        output = ''

        for guild in self.guilds:
            if guild.getGuildId() == guildId:
                output = guild.getNotesFromSubject(subjectName)
                break

        if output == '':
            output = self.noInfoAnswer

        return output
