import Command
import DocumentController

class UserController:

    def __init__(self):
        self.arguments = None

    def getArguments(self):
        return self.arguments

    def setArguments(self, arguments):
        self.arguments = arguments

    def parseArguments(self):
        pass

docCont = DocumentController.DocumentController(None)


