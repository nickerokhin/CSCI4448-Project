import cv2
import numpy as np

class Reporting:

    def viewAddResults(self, ims):
        print("Successfully added {} image(s)".format(len(ims)))
        for im in ims:
            print("Name: {}\n Tags: {}\n".format(im.getName(), im.getTags()))

    def viewImages(self, ims):

        for im in ims:
            docPath = im.getDocumentPath()
            img = cv2.imread(docPath, 0)
            imName = im.getName()
            cv2.imshow(imName, img)
            



    


