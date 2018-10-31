import requests 
import json
import base64


class DocumentController:


    def __init__(self, documents):
        self.__documents = documents
        self.__credentials = json.loads(open("apicreds.json", "r").read())
        self.__APIKEY = self.__credentials["api_key"]
        

    def addDocument(self, docPath):
        self.__documents.append(docPath)

    def removeDocument(self, docPath):
        self.__documents.remove(docPath)

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
            print(tags)


    def uploadCSV(self, csvPath):
        pass

    def downloadImage(self, imageName):
        pass 

    def viewImage(self, imageName):
        pass




doc = DocumentController(None)
doc.getTagsFromCloud("tesimg.jpg")