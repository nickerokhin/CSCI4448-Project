
class SearchResults:

    def __init__(self, queryResults, threshold, queryTags):

        self.__queryResults = queryResults
        self.__threshold = threshold
        self.__numResults = len(queryResults)
        self.__queryTags = queryTags
        self.__numDispResults = 3

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
        print("Your query was {}".format(" ".join(self.__queryTags)))
        print("Showing top {} results for your query\n".format(self.__numDispResults))
        
        for i in self.__queryResults[:self.__numDispResults]:
            print(i + "\n")


