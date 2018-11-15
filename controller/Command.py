import abc
from views.SearchResults import SearchResults

class Invoker:

    def __init__(self):
        self.__commands = []
    
    def storeCommand(self, command):
        self.__commands.append(command)

    def executeCommands(self):
        while len(self.__commands):
            cmd = self.__commands.pop()
            cmd.execute()


class CommandFactory:

    def __init__(self, searchIndex, documentController, invoker):
        self.__searchIndex = searchIndex
        self.__documentController = documentController
        self.__invoker = invoker

    def factory(self, typ):
        if typ[0] == "search":
            return Search(typ[1], self.__searchIndex)

    def makeCommandsFromArguments(self, args):
        for arg in args:
            self.__invoker.storeCommand(self.factory(arg))
        return self.__invoker







class Search:

    def __init__(self, query, searchIndex):
        self.__query = query
        self.__searchIndex = searchIndex

    def execute(self):
        print(self.__searchIndex)
        results = self.__searchIndex.search(self.__query)
        resultImages = self.__searchIndex.listResultIms(results)
        searchResults = SearchResults(resultImages, None, self.__query)
        searchResults.displayResults()
