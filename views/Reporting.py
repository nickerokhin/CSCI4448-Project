class Reporting:

    def viewAddResults(self, ims):
        print("Successfully added {} image(s)".format(len(ims)))
        for im in ims:
            print("Name: {}\n Tags: {}\n".format(im.getName(), im.getTags()))

    


