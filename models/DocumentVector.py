class DocumentVector:

    def __init__(self, tags, imagePath, vector, vectorSize, relevanceThreshold):
        self.__tags = tags
        self.__imagePath = imagePath
        self.__vector = vector
        self.__vectorSize = vectorSize
        self.__relevanceThreshold = relevanceThreshold


    def getTags(self):
        return self.__tags

    def setTags(self,tags):
        self.__tags = tags

    def getImagePath(self):
        return self.__imagePath

    def getVector(self):
        return self.__vector

    def createCustomVectorFromTags(self, tags):
        pass

    def setVector(self, vec):
        self.vector = vec
