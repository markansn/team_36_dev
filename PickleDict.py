import pickle
import os
import datetime
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






"""

USE THESE THREE FUNCTIONS 

"""
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



