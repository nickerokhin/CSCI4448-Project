
class SearchResults:

    def __init__(self, queryResults, threshold, queryTags):

        self.__queryResults = queryResults
        self.__threshold = threshold
        self.__numResults = len(queryResults)
        self.__queryTags = queryTags

    def getNumResults(self):
        return self.__numResults
    
    def setNumResults(self, num):
        self.__numResults = num

    def setQueryResults(self, queryResults):
        self.__queryResults =  queryResults

    def setThreshold(self, thresh):
        self.__threshold = thresh

    def getThreshold(self):
        return self.__threshold

    def filterResults(self):
        pass

    def newQuery(self):
        pass 

    def displayResults(self):
        pass


