class Document:


    def __init__(self, documentPath, locallyHosted, cloudHosted, name):
        self.__documentPath = documentPath
        self.__locallyHosted = locallyHosted
        self.__cloudHosted = cloudHosted
        self.__name = name


    def getDocumentPath(self):
        return self.__documentPath


    def setDocumentPath(self, path):
        self.__documentPath = path


    def isLocallyHosted(self):
        return self.__locallyHosted


    def isCloudHosted(self):
        return self.__cloudHosted


    def getName(self):
        return self.__name

    def setName(self, name):
        pass