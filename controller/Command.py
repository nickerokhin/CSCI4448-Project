import abc
from views.SearchResults import SearchResults
from views.Reporting import Reporting
from controller.DocumentController import DocumentController

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

        elif typ[0] == "addImage":
            return AddImage(typ[1], self.__searchIndex, self.__documentController)

        elif typ[0] == "addImageBulk":
            return AddImageBulk(typ[1], self.__searchIndex,  self.__documentController)

        elif typ[0] == "displayImages":
            return DisplayImages(typ[1], self.__searchIndex, self.__documentController)

    def makeCommandsFromArguments(self, args):
        for arg in args:
            self.__invoker.storeCommand(self.factory(arg))
        return self.__invoker







class Search:

    def __init__(self, query, searchIndex):
        self.__query = query
        self.__searchIndex = searchIndex

    def execute(self):
        results = self.__searchIndex.search(self.__query)
        resultImages = self.__searchIndex.listResultIms(results)
        searchResults = SearchResults(resultImages, None, self.__query)
        searchResults.displayResults()
        self.__searchIndex.setMostRecentResults(results)


class AddImage:

    def __init__(self, imPath, searchIndex, documentController):
        self.__imPath = imPath
        self.__searchIndex = searchIndex
        self.__documentController = documentController

    def execute(self):
        
        #First get tags from cloud
        tags = self.__documentController.getTagsFromCloud(self.__imPath)
        #Next, we need to create the Document Object for this particular document
        doc = self.__documentController.createDocument(self.__imPath, tags)
        #Now that we have the document, we must add it to the search index
        self.__documentController.addDocumentToIndex(doc)
        reporter = Reporting()
        reporter.viewAddResults([doc])

class AddImageBulk:

    def __init__(self, ims, searchIndex, documentController):
        self.__ims = ims
        self.__searchIndex = searchIndex
        self.__documentController = documentController

    def execute(self):
        pass
        #for im in self.__ims

class DisplayImages:

    def __init__(self, results, searchIndex, documentController):
        self.__results = results
        self.__searchIndex = searchIndex
        self.__documentController = documentController

    def execute(self):
        reporter = Reporting()
        reporter.viewImages(self.__results)





