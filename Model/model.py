import discord
from Model.fileHandler import *
from Model.guildNode import *

class Model:
    def __init__(self):
        self.errColor = discord.Colour.from_rgb(225, 7, 0)
        self.defColor = discord.Colour.from_rgb(0, 239, 134)
        self.prefix = '!'
        self.helpStatus = True
        self.guilds = []
        self.fileName = 'memory.json'
        
        self.__buildGuilds()

    # Getters and setters

    def getPrefix(self) -> str:
        return self.prefix

    def getErrorColor(self) -> discord.Colour:
        return self.errColor

    def getDefaultColor(self) -> discord.Colour:
        return self.defColor
    
    def getCommandHelpStatus(self) -> bool:
        return self.helpStatus

    # File management

    def __readData(self) -> dict:
        fileHandler = FileHandler()
        return fileHandler.readJSON(self.fileName)

    def __writeData(self, info: dict) -> bool:
        fileHandler = FileHandler()
        return fileHandler.writeJSON(self.fileName, info)

    # Guilds management

    def __buildGuilds(self):
        # Read json and generate objects
        pass

    def __verifyGuildExistence(self, guildId) -> bool:
        exists = False

        for guild in self.guilds:
            if guild.getGuildId == guildId:
                exists = True
                break

        return exists

    def __updatePersistentData(self) -> bool:
        listDict = []

        for guild in self.guilds:
            listDict.append(guild.toDict())

        return self.__writeData({"Guilds" : listDict})

    def addGuild(self, guildId: int) -> bool:
        flag = True

        try:
            if not self.__verifyGuildExistence():
                g = GuildNode(guildId)
                self.guilds.append(g)
        except:
            flag = False

        return flag
