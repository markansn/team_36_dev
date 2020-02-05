import os
import sys
import Model
import HandleDictionary

def getPathAndFile():
    return input("Path: "), input("Name: ")


def train():
    print("please copy the file to the folder named \"TrainingInputFolder\"")
    input("please press enter after you done that")

    pathname = os.path.dirname(sys.argv[0])
    pathname = os.path.abspath(pathname) + os.path.sep + "TrainingInputFolder"

    Model.trainningWithPath(pathname)


def extract():
    pathname = os.path.dirname(sys.argv[0])
    pathname = os.path.abspath(pathname) + os.path.sep + "ExtractionInputFolder"

    print(Model.extractWithPath(pathname))



def storeTrainingData():
    dirPath, fileName = getPathAndFile()
    HandleDictionary.storeTrainingData(Model.keywordDict, Model.generalDict, dirPath, fileName)

def fetchTrainingData():
    dirPath, fileName = getPathAndFile()
    Model.keywordDict, Model.generalDict = HandleDictionary.fetchTrainingData(dirPath, fileName)
    print(Model.keywordDict)

def revert():
    dirPath, fileName = getPathAndFile()
    HandleDictionary.revert(dirPath, fileName)





def main():
    configurationFile = open("configuration.txt", "r")
    subscription_key = configurationFile.readline().rstrip("\n\r")
    endpoint = configurationFile.readline().rstrip("\n\r")
    configurationFile.close()
    ocr_url = endpoint + "vision/v2.1/ocr"

    Model.assaginaAuthenticationCredentials(subscription_key, endpoint, ocr_url)
    loop = True
    while loop:
        print(
            "Please enter a number to select an option: \n 1:Use a group of data to train the algorithm \n 2:Extract information out of a document \n\n 3:save current dictionary to local disk \n 4:Load dictionary from local disk \n 5:undo last training \n 6:Exit\n")
        mainOption = input("Your choice: ")
        if mainOption == "1":
            train()

        elif mainOption == "2":
            extract()

        elif mainOption == "3":
            storeTrainingData()

        elif mainOption == "4":
            fetchTrainingData()
            print("---")
            print(Model.keywordDict)

        elif mainOption == "5":
            revert()

        elif mainOption == "6":
            loop = False

        else:
            print(
                "Invalid input. Please make sure you input the correct number, and no space or other symbol before and after that")












if __name__ == "__main__":
    main()