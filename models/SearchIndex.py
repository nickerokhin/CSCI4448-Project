from models.DocumentVector import DocumentVector
import numpy as np
from scipy import spatial



class SearchIndex:
    __instance = None

    @staticmethod
    def getInstance():
        if SearchIndex.__instance == None:
            SearchIndex()
        return SearchIndex.__instance

    def __init__(self, columnSize = None, documentCount = None, documentMatrixMap = None, \
                documentMap = None, tagVectorIndexMap = None, threshold = None):

        if SearchIndex.__instance != None:
            raise Exception("What are you doing")
        else:
            SearchIndex.__instance = self

        self.__documentMatrix = None

        self.__columnSize = columnSize
        self.__documentMatrixMap = {}
        self.__documentMap = documentMap
        self.__tagVectorIndexMap = {}
        self.__threshold = threshold
        self.__documentCount = documentCount
        self.__vectorSize = None


    def createVectorIndexMap(self, documents):
        tags = []
        for doc in documents:
            tags += doc.getTags()

        tags = list(set(tags))
        for tagIdx in range(0, len(tags)):
            self.__tagVectorIndexMap[tags[tagIdx]] = tagIdx

        self.__vectorSize = len(self.__tagVectorIndexMap)
        print(self.__tagVectorIndexMap)

    def createDocumentMatrixMap(self, documents):
        for doc in range(0, len(documents)):
            self.__documentMatrixMap[doc] = documents[doc].getDocumentPath()

        print(self.__documentMatrixMap)


    def createDocumentVector(self, document):
        vec = np.zeros(self.__vectorSize)

        for tag in document.getTags():
            vec[self.__tagVectorIndexMap[tag]] = 1

        return vec
            

    def constructDocumentMatrix(self, documents):
        self.__documentMatrix = np.zeros((self.__documentCount, self.__vectorSize))
        for idx in range(0, len(documents)):
            self.__documentMatrix[idx] = self.createDocumentVector(documents[idx])

        print(self.__documentMatrix)
        
    def constructQueryVector(self, queryTerms):
        #This could be more robust, for demo purposes only
        vec = np.zeros(self.__vectorSize)
        for q in queryTerms:
            if q in self.__tagVectorIndexMap:
                vec[self.__tagVectorIndexMap[q]] = 1
        return vec

    def addDocument(self, vector):
        pass

    def addDocumentVector(self, vector):
        pass

    def addTagToIndex(self, tag):
        pass

    def removeTagFromIndex(self, tag):
        pass

    def getColumnSize(self, tag):
        pass

    def setColumnSize(self, tag):
        pass

    def getDocumentCount(self):
        return self.__documentCount

    def setDocumentCount(self, count):
        self.__documentCount = count

    def search(self, queryTerms):
        queryVector = self.constructQueryVector(queryTerms)
        results = []
        for idx in range(0, self.__documentMatrix.shape[0]):
            results.append((1 - spatial.distance.cosine(queryVector, self.__documentMatrix[idx]), idx))
        sortedResults = sorted(results, key = lambda x: x[0], reverse = True)
        return sortedResults

    #TODO Implement this in SearchResults Class
    def listResultIms(self, results):
        res = [self.__documentMatrixMap[tup[1]] for tup in results]
        return res

    def saveMatrix(self):
        pass

    def loadMatrix(self):
        pass

