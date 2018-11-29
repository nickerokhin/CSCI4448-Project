import cv2
import numpy as np

class Reporting:

    def viewAddResults(self, ims):
        print("Successfully added {} image(s)".format(len(ims)))
        for im in ims:
            print("Name: {}\n Tags: {}\n".format(im.getName(), im.getTags()))

    def viewImages(self, ims):

        for im in ims:
            im = "./ims/" + im
            img = cv2.imread(im, 0)
            imName = im.split("/")[-1]
            cv2.namedWindow(imName, cv2.WINDOW_NORMAL)
            cv2.imshow(imName, img)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def listResults(self, res):
        print("Listing documents:")
        for r in res:
            print(r.getName())







