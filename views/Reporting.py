import cv2
import numpy as np

class Reporting:

    def viewAddResults(self, ims):
        print("Successfully added {} image(s)".format(len(ims)))
        for im in ims:
            print("Name: {}\n Tags: {}\n".format(im.getName(), im.getTags()))

    def printTags(self, tags):
        print(', '.join(tags))

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

    def printMan(self):
        print('''
To search for an image using tags, format your query like so:

- search q/ term1, term2, term3 /q

To add an image to the index, format your query like so:

- add {num to add} pic1.jpg pic2.jpg

To save the search index to disk, type 'save'

To view the images from the search results, format your query like so:

- showResultIms {num of images to show}

To list all documents in the index, type 'ls'

You able to stack commands as well.
If you want to add images and save the index with one command, the following will work

- add 2 pic1.jpg pic2.jpg save
        ''')







