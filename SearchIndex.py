from DocumentVector import DocumentVector
import numpy as np



class SearchIndex:

    def __init__(self, documentMatrix, columnSize, documentCount, documentMatrixMap, \
                documentMap, tagVectorIndexMap, threshold, documentCount):

        self.__documentMatrix = documentMatrix
        self.__columnSize = columnSize
        self.__documentMatrixMap = documentMatrixMap
        self.__documentMap = documentMap
        self.__tagVectorIndexMap = tagVectorIndexMap
        self.__threshold = threshold
        self.__documentCount = documentCount


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
        self.__documentCount += count

    def search(self, queryVector):
        pass

    def saveMatrix(self):
        pass

    def loadMatrix(self):
        pass

