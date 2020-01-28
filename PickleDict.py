import pickle
import os
def convertToPickleFromDict(dict, filename):
    with open(filename + '.pickle', 'wb') as handle:
        pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


def convertToDictFromPickle(filename):
    with open(filename + '.pickle', 'rb') as handle:
        p = pickle.load(handle)

    os.remove(filename + '.pickle')
    return p




