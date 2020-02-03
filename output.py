import os
import sys

import MainDev

configurationFile = open("configuration.txt", "r")
subscription_key = configurationFile.readline().rstrip("\n\r")
endpoint = configurationFile.readline().rstrip("\n\r")
configurationFile.close()
ocr_url = endpoint + "vision/v2.1/ocr"

MainDev.assaginaAuthenticationCredentials(subscription_key, endpoint, ocr_url)
loop = True
while loop:
    print("Please enter a number to select an option: \n 1:Use a group of data to train the algorithm \n 2:Extract information out of a document \n\n 3:save current dictionary to local disk \n 4:Load dictionary from local disk \n 5:undo last training \n 6:Exit\n")
    mainOption = input("Your choice: ")
    if mainOption == "1":
        print("please copy the file to the folder named \"TrainingInputFolder\"")
        input("please press enter after you done that")

        pathname = os.path.dirname(sys.argv[0])
        pathname = os.path.abspath(pathname) + os.path.sep + "TrainingInputFolder"

        MainDev.trainningWithPath(pathname)

    elif mainOption == "2":
        pathname = os.path.dirname(sys.argv[0])
        pathname = os.path.abspath(pathname) + os.path.sep + "ExtractionInputFolder"

        print(MainDev.extractWithPath(pathname))

    elif mainOption == "3":
        dirPath = input("Path: ")
        FileName = input("Name: ")
        #MainDev.

    # elif mainOption == "4":
    #     #read local

    # elif mainOption == "5":
    #     #undo last train

    elif mainOption == "6":
        loop = False

    else:
        print(
            "Invalid input. Please make sure you input the correct number, and no space or other symbol before and after that")
