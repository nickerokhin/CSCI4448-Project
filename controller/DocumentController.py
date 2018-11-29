import requests
import sys
sys.path.append('../')
sys.path.append('../models')
import json
import base64
from models.Image import Image
import os
import pickle

class DocumentController:


    def __init__(self, documents, searchIndex):
        self.__documents = documents
        self.__credentials = json.loads(open("./controller/apicreds.json", "r").read())
        self.__APIKEY = self.__credentials["api_key"]
        self.__searchIndex = searchIndex
        self.__picklePath = "./controller/pickedims"

    def createDocument(self, docPath, tags):
        newDoc = Image(docPath, True, False, docPath.split("/")[-1], tags)
        return newDoc

    def addDocument(self, document):
        self.__documents.append(document)


    def addDocumentToIndex(self, document):
        self.addDocument(document)
        self.__searchIndex.createVectorIndexMap(self.__documents)
        self.__searchIndex.setDocumentCount(len(self.__documents))
        self.__searchIndex.createDocumentMatrixMap(self.__documents)
        self.__searchIndex.constructDocumentMatrix(self.__documents)

    def addDocumentToIndexBatch(self, documents):
        pass

    def saveDocuments(self):
        out = open(self.__picklePath, "wb")
        pickle.dump(self.__documents, out)
        out.close()

    def removeDocument(self, docPath):
        self.__documents.remove(docPath)

    def addDocuments(self, docArray):
        self.__documents += docArray

    def getDocuments(self):
        return self.__documents
    #def getb64encoding(self, docPath):


    def uploadDocument(self, docPath):
        pass

    def getTagsFromCloud(self, docPath):
        with open(docPath, "rb") as im:
            body = {
                "requests":[
                    {
                    "image":{
                        "content": base64.b64encode(im.read()).decode('utf-8')
                    },
                    "features": [
                        {
                        "type":"LABEL_DETECTION"
                        }
                    ]
                    }
                ]
                }
            url = "https://vision.googleapis.com/v1/images:annotate?key={}".format(self.__APIKEY)
            r = requests.post(url, data = json.dumps(body))
            r = r.json()
            tags = [ann["description"] for ann in r['responses'][0]['labelAnnotations']]
            return tags



    def uploadCSV(self, csvPath):
        pass

    def downloadImage(self, imageName):
        pass 

    def viewImage(self, imageName):
        pass


'''
doc = DocumentController(None, None)
imList = os.listdir('../ims')
tagsArray = [doc.getTagsFromCloud("../ims/" + path) for path in imList]
ImagesArray = [Image("./ims/" + imList[path], True, False, imList[path], tagsArray[path]) for path in range(0, len(tagsArray))]
out = open("pickedims", "wb")
pickle.dump(ImagesArray, out)
out.close()

infile = open("pickedims", "rb")
ImagesArray = pickle.load(infile)
infile.close()
doc.addDocuments(ImagesArray)
docs = doc.getDocuments()
searchIndex = SearchIndex()
searchIndex.createVectorIndexMap(docs)
searchIndex.setDocumentCount(len(docs))
searchIndex.createDocumentMatrixMap(docs)
searchIndex.constructDocumentMatrix(docs)
queryVector = ["t shirt", "arm", "technology", "product"]
results = searchIndex.search(queryVector)
out = open("searchindex", "wb")
pickle.dump(searchIndex, out)
out.close()

print(searchIndex.listResultIms(results))
#searchIndex.createDocumentVector(docs[0])
'''