from DocumentVector import DocumentVector
import numpy as np
from scipy import spatial



class SearchIndex:

    def __init__(self, columnSize = None, documentCount = None, documentMatrixMap = None, \
                documentMap = None, tagVectorIndexMap = None, threshold = None):

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
        pass

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

    def search(self, queryVector):
        pass

    def saveMatrix(self):
        pass

    def loadMatrix(self):
        pass

