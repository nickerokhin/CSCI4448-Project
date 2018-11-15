import abc
from views.SearchResults import SearchResults

class Invoker:

    def __init__(self):
        self.__commands = []
    
    def storeCommand(self, command):
        self.__commands.append(command)

    def executeCommands(self):
        for command in self.__commands:
            command.execute()


class CommandFactory():

    def __init__(self, searchIndex, documentController):
        self.__searchIndex = searchIndex
        self.__documentController = documentController

    def factory(self, typ):
        if typ[0] == "search":
            return Search(typ[0], self.__searchIndex)

    def makeCommandsFromArguments(self, args):
        invoker = Invoker()
        for arg in args:
            invoker.storeCommand(self.factory(arg))
        return invoker







class Search():

    def __init__(self, query, searchIndex):
        self.__query = query
        self.__searchIndex = searchIndex

    def execute(self):
        results = self.__searchIndex.search(query)
        resultImages = self.__searchIndex.listResultIms(results)
        searchResults = SearchResults(resultImages, None, self.__query)
        searchResults.displayResults()
