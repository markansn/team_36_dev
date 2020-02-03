import requests
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import json

import os
import sys


def authenticateClient():
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credentials=credentials)
    return text_analytics_client

def key_phrases(doc):
    client = authenticateClient()

    #print('keyphase', ConvertToJSON(doc))
    try:
        response = client.key_phrases(documents=json.loads(ConvertToJSON(doc)))
        return response.documents
    except Exception as err:
        print("Encountered exception. {}".format(err))

def ConvertToJSON(OCRout):
    temp = json.dumps(eval(str(OCRout)))
    return str(temp)

def parseStringToInt(array1, array2):
    for i in range(len(array1)):
        array1[i] = int(array1[i])
    for i in range(len(array2)):
        array2[i] = int(array2[i])
    return array1, array2

def inTheSameParagraph(array1, array2):
    array1,array2 = parseStringToInt(array1, array2)

    limit = 30

    leftBondA1 = array1[0]
    topBondA1 = array1[1]
    widthA1 = array1[2]
    heightA1 = array1[3]

    leftBondA2 = array2[0]
    topBondA2 = array2[1]
    widthA2 = array2[2]
    heightA2 = array2[3]

    if abs((leftBondA1+widthA1)-leftBondA2)<limit:
        return True
    elif abs((leftBondA2+widthA2)-leftBondA1)<limit:
        return  True
    elif abs((topBondA1+heightA1)-topBondA2)<limit:
        return True
    elif abs((topBondA2+heightA2)-topBondA1)<limit:
        return True
    else:
        return False

def OCR2KeyPhrasesReFormatter(OCRout):
    outputBuffer  = []
    outputString = ""
    resp_dict = json.loads(OCRout)
    temp = ConvertToJSON(resp_dict.get('regions'))
    id = 0

    resp_dict = json.loads(temp)
    for JSONObj in resp_dict:
        temp = JSONObj.get('lines')
        endPosOfLastLine = None

        for str in temp:
            singleLine = json.loads(ConvertToJSON(str))
            words = singleLine.get('words')
            PosOfTheFirst = json.loads(ConvertToJSON(words[0])).get('boundingBox').split(",")
            if endPosOfLastLine == None or inTheSameParagraph(endPosOfLastLine,PosOfTheFirst):
                for word in words:
                    wordJSON = json.loads((ConvertToJSON(word)))
                    text = wordJSON.get('text')
                    outputString += text + " "
                endPosOfLastLine = json.loads(ConvertToJSON(words[len(words)-1])).get('boundingBox').split(",")
            else:
                temp = json.dumps({'id': id, 'language': 'en', 'text':outputString})
                id = id + 1
                outputBuffer.append(json.loads(temp))
                outputString = ""
                for word in words:
                    wordJSON = json.loads((ConvertToJSON(word)))
                    text = wordJSON.get('text')
                    outputString += text + " "
                endPosOfLastLine = json.loads(ConvertToJSON(words[len(words)-1])).get('boundingBox').split(",")
        temp = json.dumps({'id': id, 'language': 'en', 'text': outputString})
        id = id + 1
        outputString = ""
        outputBuffer.append(json.loads(temp))

    return outputBuffer

def callForEachWord(dict, json_text):
    json_dict = json.loads(json_text)
    regions = json_dict['regions']

    for region in regions:
        lines = region['lines']
        for line in lines:
            words = line['words']
            for word in words:
                increaseCounter(dict, word['text'])

def callForEachWordScore(dict, json_text):
    json_dict = json.loads(json_text)
    regions = json_dict['regions']
    scoreDel = 0;

    for region in regions:
        lines = region['lines']
        for line in lines:
            words = line['words']
            for word in words:
                if(search_dict(dict, word['text'])):
                    scoreDel += 5;
    return scoreDel

def search_dict(inputdict, key):
    if key in inputdict:
        return True
    return False

def increaseCounter(inputdict, key):
    if(search_dict(inputdict, key)):
        inputdict[key] += 1
    else:
        inputdict[key] = 1

def getTopValue(dictionary, num_of_items):
    sorted_dict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse = True)}

    first_x_pairs = {k: sorted_dict[k] for k in list(sorted_dict)[:num_of_items]}

    return first_x_pairs

def OCR(image_path):
    # Read the image into a byte array
    image_data = open(image_path, "rb").read()

    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    params = {'language': 'unk', 'detectOrientation': 'true'}
    data = image_data
    response = requests.post(ocr_url, headers=headers, params=params, data=data)
    response.raise_for_status()

    return response

def callForEachWordKey(dict, json_text):
    json_text = ConvertToJSON(json_text.replace("None", "\"None\""))
    json_dict = json.loads(ConvertToJSON(json_text))
    key_phrases = json_dict['key_phrases']
    for phrase in key_phrases:
        for word in phrase.split():
            increaseCounter(dict, word)

def callForEachWordKeyReal(dict, json_text):
    json_text = ConvertToJSON(json_text.replace("None", "\"None\""))
    json_dict = json.loads(ConvertToJSON(json_text))
    key_phrases = json_dict['key_phrases']
    scoreDel = 0;
    for phrase in key_phrases:
        if search_dict(dict, phrase):
            scoreDel += 10;
    return  scoreDel

def callForEachWordRealOriginal(inputdict, json_text):
    json_dict = json.loads(json_text)
    regions = json_dict['regions']
    scoreDel = 0

    for region in regions:
        lines = region['lines']
        for line in lines:
            words = line['words']
            for word in words:
                if(search_dict(inputdict, word['text'])):
                    scoreDel += 3
    return scoreDel

#global Vars
limit = 20
score = 0


subscription_key = "ffcc4bbd174c4b6e97d0a945aebf8b98"
endpoint = "https://uksouth.api.cognitive.microsoft.com/"

ocr_url = endpoint + "vision/v2.1/ocr"

# Set image_path to the local path of an image that you want to analyze.
trainingPath = "C:/Users/liu87/Desktop/UN project/Python 3.7 code src/image/Financial.PNG"

#realDataPath = "C:/Users/liu87/Desktop/UN project/Python 3.7 code src/image/NoFin.jpg"
realDataPath = "C:/Users/liu87/Desktop/UN project/Python 3.7 code src/image/bug.png"

analysis = OCR(trainingPath).json()
analysis = ConvertToJSON(analysis)
analyisReformedForKeyPhases =OCR2KeyPhrasesReFormatter(analysis)
keywordsList = key_phrases(analyisReformedForKeyPhases)   

#building dict
generalDict = {}
keywordDict = {}
#General
callForEachWord(generalDict, analysis)
generalDict = getTopValue(generalDict, 200)
#Key
for keywords in keywordsList:
    callForEachWordKey(keywordDict, str(keywords))
keywordDict = getTopValue(keywordDict, 200)
print('keyword dictionary',keywordDict)
print('general dictionary',generalDict)

new_analysis = OCR(realDataPath).json()
new_analysis = ConvertToJSON(new_analysis)
analyisReformedForKeyPhasesReal =OCR2KeyPhrasesReFormatter(new_analysis)
keywordsListReal = key_phrases(analyisReformedForKeyPhasesReal)

for keywordsReal in keywordsListReal:
    score += callForEachWordKeyReal(keywordDict, str(keywordsReal))
print ('key word matching score:', score)
generalScore = 0
generalScore += callForEachWordRealOriginal(generalDict, new_analysis)
print ('general matching score:', generalScore)
score += generalScore
print ('final score:', score)