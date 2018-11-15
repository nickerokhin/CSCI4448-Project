import os
import sys
import pickle


sys.path.append('./')
sys.path.append('./controller/')
sys.path.append('./models/')
sys.path.append('./views/')

from controller.Command import CommandFactory
from controller.UserController import UserController

infile = open("./controller/pickedims", "rb")
ImagesArray = pickle.load(infile)
infile.close()
files = os.listdir("./controller/")
if "searchindex" in files:
    with open("./controller/searchindex", "rb") as p:
        searchIndex = pickle.load(p)
else:
    from models.SearchIndex import SearchIndex

    searchIndex = SearchIndex()
    searchIndex.createVectorIndexMap(ImagesArray)
    searchIndex.setDocumentCount(len(ImagesArray))
    searchIndex.createDocumentMatrixMap(ImagesArray)
    searchIndex.constructDocumentMatrix(ImagesArray)


if __name__ == "__main__":
    userCont = UserController(ImagesArray, searchIndex)
    print('''Welcome to ImageSearch. \nYou have {} images in the index\nFor instructions, type "man"\nPlease type your instructions below...
                 
                 
                  '''.format(5))

    print(searchIndex.getDocumentCount())
    while True:
        args = input(">")

        userCont.setArguments(args)
        args = userCont.parseArguments()
        inv = userCont.createCommands(args)
        userCont.executeInvokerCommands(inv)



