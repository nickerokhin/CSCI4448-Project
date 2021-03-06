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
            cmd = self.__commands.pop(0)
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

        elif typ[0] == "save":
            return Save(self.__searchIndex, self.__documentController)
            
        elif typ[0] == "list":
            return List(self.__documentController.getDocuments())

        elif typ[0] == "man":
            return Manual()

        elif typ[0] == "tags":
            return Tags(self.__searchIndex)

    def makeCommandsFromArguments(self, args):
        for arg in args:
            self.__invoker.storeCommand(self.factory(arg))
        return self.__invoker




class Command(object):

    def execute(self):
        pass


class Search(Command):

    def __init__(self, query, searchIndex):
        self.__query = query
        self.__searchIndex = searchIndex

    def execute(self):
        results = self.__searchIndex.search(self.__query)
        resultImages = self.__searchIndex.listResultIms(results)
        searchResults = SearchResults(resultImages, None, self.__query)
        searchResults.displayResults()
        self.__searchIndex.setMostRecentResults(resultImages)


class AddImage(Command):

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

class AddImageBulk(Command):

    def __init__(self, ims, searchIndex, documentController):
        self.__ims = ims
        self.__searchIndex = searchIndex
        self.__documentController = documentController

    def execute(self):
        
        allDocs = []
        for im in self.__ims:
            tags = self.__documentController.getTagsFromCloud(im)
            doc = self.__documentController.createDocument(im, tags)
            self.__documentController.addDocumentToIndex(doc)
            allDocs.append(doc)
        reporter = Reporting()
        reporter.viewAddResults(allDocs)

        


class DisplayImages(Command):

    def __init__(self, num, searchIndex, documentController):
        self.__num = num
        self.__searchIndex = searchIndex
        self.__documentController = documentController

    def execute(self):
        reporter = Reporting()
        results = self.__searchIndex.getMostRecentResults()
        reporter.viewImages(results[:self.__num])

class Save(Command):
    
    def __init__(self, searchIndex, documentController):
        self.__searchIndex = searchIndex
        self.__documentController = documentController

    def execute(self):
        print("Saving search index...")
        self.__searchIndex.saveMatrix()
        print("Search index saved")
        print("Saving images...")
        self.__documentController.saveDocuments()
        print("Images saved successfully")

class List(Command):

    def __init__(self, ls):
        self.__ls = ls

    def execute(self):
        reporter = Reporting()
        reporter.listResults(self.__ls)

class Manual(Command):

    def execute(self):
        reporter = Reporting()
        reporter.printMan()

class Tags(Command):

    def __init__(self, searchIndex):
        self.__searchIndex = searchIndex 

    def execute(self):
        tags = self.__searchIndex.getAllTags()
        reporter = Reporting()
        reporter.printTags(tags)
        







