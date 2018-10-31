from Document import Document


class Image(Document):

    def __init__(self, documentPath, locallyHosted, cloudHosted, name, tags):
        super().__init__(documentPath, locallyHosted, cloudHosted, name)
        self.__tags = tags

    def getTags(self):
        return self.__tags

    def setTags(self, tags):
        self.__tags = tags

    def addTags(self, tags):
        #Tags should be an array
        self.__tags += tags

        
        