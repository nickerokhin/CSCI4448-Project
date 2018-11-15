import requests 
import json
import base64
from Image import Image
import os
import pickle
from SearchIndex import SearchIndex

class DocumentController:


    def __init__(self, documents):
        self.__documents = []
        self.__credentials = json.loads(open("apicreds.json", "r").read())
        self.__APIKEY = self.__credentials["api_key"]
        

    def addDocument(self, docPath):
        self.__documents.append(docPath)

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




#imList = os.listdir('./ims')
doc = DocumentController(None)
#tagsArray = [doc.getTagsFromCloud("./ims/" + path) for path in imList]
#ImagesArray = [Image(imList[path], True, False, "./ims/" + imList[path], tagsArray[path]) for path in range(0, len(tagsArray))]
#out = open("pickedims", "wb")
#pickle.dump(ImagesArray, out)
#out.close()
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

print(searchIndex.listResultIms(results))
#searchIndex.createDocumentVector(docs[0])