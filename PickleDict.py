import pickle
import os
import datetime


"""

USE THESE FUNCTIONS 

"""





def storeTrainingData(keywordDict, generalDict, directory, filename):

    createPickle([keywordDict, generalDict], directory, filename)

def fetchTrainingData(directory, filename):
    data = getPickle(directory, filename)
    return data[0], data[1]



# Fetch pickle


def fetch(directory, filename):

    return getPickle(directory, filename)[-1]


# Store pickle


def store(dictionary, directory, filename):

    createPickle(dictionary, directory, filename)


# Delete most recent pickle entry


def revert(directory, filename):

    p = getPickle(directory, filename)
    if len(p) > 1:
        p.pop(-1)
    path = os.path.join(directory, filename + "." + "pickle")
    os.remove(path)
    with open(path, 'wb') as handle:
        pickle.dump(p, handle, protocol=pickle.HIGHEST_PROTOCOL)







def createPickle(dictionary, directory, filename):
    MAX_DICT_NUMBER = 5
    path = os.path.join(directory, filename + "." + "pickle")
    print(path)
    dict_list = []
    if os.path.exists(path):
        currentList = getPickle(directory, filename)

        if len(currentList) == MAX_DICT_NUMBER:
            currentList.pop(0)

        currentList.append(dictionary)
        dict_list = currentList

    else:
        dict_list = [dictionary]

    with open(path, 'wb') as handle:
        pickle.dump(dict_list, handle, protocol=pickle.HIGHEST_PROTOCOL)


def getPickle(directory, filename):
    path = os.path.join(directory, filename + "." + "pickle")
    with open(path, 'rb') as handle:
        p = pickle.load(handle)


    return p





# def main():
#     trainingData = {
#         1: "train",
#         2: "data"
#     }
#
#     generalData = {
#         1: "car",
#         2: "information"
#     }
#
#     createPickle([trainingData, generalData], "/Users/markanson/dev/team_36_dev/pickles/", "example")
#     print(getPickle("/Users/markanson/dev/team_36_dev/pickles/", "example"))
#
#
# main()