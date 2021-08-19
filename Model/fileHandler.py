import json

class FileHandler:
    def __init__(self):
        pass

    def readJSON(self, fileName: str) -> dict:
        output = None

        try:
            with open(fileName, 'r') as f:
                output = json.load(f)
        except:
            output = {}

        return output

    def writeJSON(self, fileName: str, info: dict) -> bool:
        output = True

        try:
            with open(fileName, 'w') as f:
                f.write(json.dumps(info, indent=2))
        except:
            output = False

        return output
