import Model
import pandas as pd
import glob
import json
import string
import os
from io import BytesIO
from PIL import Image
import sys
# import nltk
# from nltk.corpus import words as nltk_words
# nltk.download('words')
# dictionary = dict.fromkeys(nltk_words.words(), None)

# def is_english_word(word): #credit https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
#
#     try:
#         x = dictionary[word]
#         return True
#     except KeyError:
#         return False


setofwords = set(line.strip() for line in open(
    'allEnglishWords.txt'))  # credit https://stackoverflow.com/questions/874017/python-load-words-from-file-into-a-set
punctuation = str.maketrans(dict.fromkeys(string.punctuation)) #credit https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string




def getImgSize(img):
    return createImageBuffer(img).tell()

def createImageBuffer(img):
    img_file = BytesIO()
    img.save(img_file, 'jpeg', quality=90)
    return img_file

def reduceImageSize(img):

    img_file = createImageBuffer(img)
    return Image.open(img_file)


def getTextFromImage(img):
    text = []


    img_file = BytesIO()
    img.save(img_file, 'jpeg')
    img_file_size = img_file.tell() #credit  https://stackoverflow.com/questions/11904083/how-to-get-image-size-bytes-using-pil


    if img_file_size < 1000000:


        img = Image.open(img_file)

        data = Model.OCR(img).json()

        data = Model.ConvertToJSON(data)

        json_dict = json.loads(data)
        regions = json_dict['regions']

        for region in regions:
            lines = region['lines']
            for line in lines:
                words = line['words']
                for word in words:
                    text.append(word['text'])
        return text
    else:
        print("!Warn: file too big to read")

    return []



def getWordsOnFirstPage(images, word_exists):
    text = []

    first_page = getTextFromImage(images[0][0])

    # for img in images[0]:
    #
    #     text = getTextFromImage(img)

    possible_names = []
    for word in first_page:
        print(word)
        # if '@' in word.lower() or "www." in word.lower() or ".org" in word.lower():
        #     print(word)


        word = word.lower().translate(punctuation)

        if word not in setofwords and not word.isdigit() and not word_exists:
            possible_names.append(word)
        elif not word.isdigit:
            possible_names.append(word)

    return possible_names


def possible_name_in_file_name(possible_names, reportName):
    for item in possible_names:
        if item in reportName.lower():
            return item
    return []

def readReport(reportName):
    images = Model.pdfsIterator([reportName])

    possible_names = getWordsOnFirstPage(images, False)
    if len(possible_names) == 0:
        return "no names found on first page"

    in_file_name = possible_name_in_file_name(possible_names, reportName)
    if not in_file_name == []:
        return in_file_name


    images[0].reverse()
    for img in images[0]:
        text = getTextFromImage(img)

        urls = []
        for word in text:
            if '@' in word.lower() or "www." in word.lower() or ".org" in word.lower():
                urls.append(word)

        for url in urls:
            for possible_name in possible_names:
                if possible_name in url:
                    return possible_name





    return "found " + str(possible_names) + " but none could be verified"
def main():
    configurationFile = open("configuration.txt", "r")
    subscription_key = configurationFile.readline().rstrip("\n\r")
    endpoint = configurationFile.readline().rstrip("\n\r")
    configurationFile.close()
    ocr_url = endpoint + "vision/v2.1/ocr"

    Model.assaginaAuthenticationCredentials(subscription_key, endpoint, ocr_url)




    files = glob.glob("reports/*.pdf")

    # for file in files:
    #     print(file)
    #     print(readReport(file))
    #     print("\n-----------------------------------------------------\n")

    print(readReport("reports/271083-FB-Annual-Report-PROOF3.pdf"))









main()

