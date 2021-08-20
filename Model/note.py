class Note:
    def __init__(self, index: int, name: str, text: str):
        self.index = index
        self.name = name
        self.text = text

    # Getters and setters

    def getIndex(self) -> int:
        return self.index

    def getName(self) -> str:
        return self.name
    
    def getText(self) -> str:
        return self.text

    def setIndex(self, index: int):
        self.index = index

    def setName(self, name: str):
        self.name = name

    def setText(self, text: str):
        self.text = text

    # Printing data

    def toString(self) -> str:
        return f'Id: {self.index}, Name: {self.name},\nNote: {self.text}'

    # Dictionary

    def toDict(self) -> dict:
        return {
            "Name" : self.name,
            "Text" : self.text 
        }
