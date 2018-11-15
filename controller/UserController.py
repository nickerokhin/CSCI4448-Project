import sys
sys.path.append('../')
sys.path.append('../models')
sys.path.append('../views')
#from controller.Command import Command
from controller.DocumentController import DocumentController
from controller.Command import *

class UserController:

    def __init__(self, documents, searchIndex):
        self.arguments = None
        self.__documents = documents
        self.__searchIndex = searchIndex
        self.__doc = DocumentController(self.__documents, self.__searchIndex)
        self.__invoker = Invoker()
        self.__commandFactory = CommandFactory(self.__searchIndex, self.__doc, self.__invoker)

    def getArguments(self):
        return self.arguments

    def setArguments(self, arguments):
        self.arguments = arguments

    def parseArguments(self):
        args = self.arguments.split(" ")
        finalArguments = []
        for i in range(0, len(args)):
            if args[i] == "search":
                if args[i + 1] == "q/":
                    #find closing tag
                    if "/q" not in args:
                        print('Invalid query, do you have the proper "q/" and "/q" tags in place?\n')
                        break

                    f = i + 2

                    while f < len(args):
                        if args[f] == "/q":
                            break
                        else:
                            f += 1

                    querytokens = args[i + 2: f]
                    querytokens = " ".join(querytokens)
                    querytokens = querytokens.split(",")
                    for i in range(0, len(querytokens)):
                        querytokens[i] = querytokens[i].strip()
                    finalArguments.append(("search", querytokens))
        return finalArguments

    def createCommands(self, arguments):
        inv = self.__commandFactory.makeCommandsFromArguments(arguments)
        return inv

    def executeInvokerCommands(self, inv):
        inv.executeCommands()


                        




