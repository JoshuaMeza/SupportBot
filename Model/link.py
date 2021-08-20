class Link:
    def __init__(self, index: int, name: str, url: str):
        self.index = index
        self.name = name
        self.url = url

    # Getters and setters

    def getIndex(self) -> int:
        return self.index

    def getName(self) -> str:
        return self.name
    
    def getUrl(self) -> str:
        return self.url

    def setIndex(self, index: int):
        self.index = index

    def setName(self, name: str):
        self.name = name

    def setUrl(self, url: str):
        self.url = url

    # Printing data

    def toString(self) -> str:
        return f'Id: {self.index}, Name: {self.name},\nLink: {self.url}'

    # Dictionary

    def toDict(self) -> dict:
        return {
            "Name" : self.name,
            "URL" : self.url 
        }
