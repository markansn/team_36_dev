import requests
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import json;

import os;
import sys;

def authenticateClient():
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credentials=credentials)
    return text_analytics_client

def key_phrases(doc):
    client = authenticateClient();

    try:
        documents = doc

        for document in documents:
            print(
                "Asking key-phrases on '{}' (id: {})".format(document['text'], document['id']))

        response = client.key_phrases(documents=documents)

        for document in response.documents:
            print("Document Id: ", document.id)
            print("\tKey Phrases:")
            for phrase in document.key_phrases:
                print("\t\t", phrase)

    except Exception as err:
        print("Encountered exception. {}".format(err))

def ConvertToJSON(OCRout):
    temp = str(OCRout)
    temp = temp.replace('\'', '\"')
    return temp

def parseStringToInt(array1, array2):
    for i in range(len(array1)):
        array1[i] = int(array1[i])
    for i in range(len(array2)):
        array2[i] = int(array2[i])
    return array1, array2

def inTheSameParagraph(array1, array2):
    array1,array2 = parseStringToInt(array1, array2);

    limit = 30;

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
    temp = temp[1:-1]
    resp_dict = json.loads(temp)
    temp = resp_dict.get('lines')
    endPosOfLastLine = None
    id = 0;
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
            outputBuffer.append(json.loads(temp))
            id += 1
            outputString = ""
            for word in words:
                wordJSON = json.loads((ConvertToJSON(word)))
                text = wordJSON.get('text')
                outputString += text + " "
            endPosOfLastLine = json.loads(ConvertToJSON(words[len(words)-1])).get('boundingBox').split(",")
    temp = json.dumps({'id': id, 'language': 'en', 'text': outputString})
    outputBuffer.append(json.loads(temp))
    return outputBuffer



#global Vars
limit = 20

# Add your Computer Vision subscription key and endpoint to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

ocr_url = endpoint + "vision/v2.1/ocr"

# Set image_path to the local path of an image that you want to analyze.
image_path = "C:/Users/liu87/Desktop/UN project/Python 3.7 code src/image/Fin1.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()

headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
params = {'language': 'unk', 'detectOrientation': 'true'}
data = image_data
response = requests.post(ocr_url, headers=headers, params=params, data=data)
response.raise_for_status()

analysis = response.json()
analysis = ConvertToJSON(analysis)
print(analysis)
#analyisReformedForKeyPhases =ConvertToJSON(OCR2KeyPhrasesReFormatter(analysis))
analyisReformedForKeyPhases =OCR2KeyPhrasesReFormatter(analysis)
print(analyisReformedForKeyPhases)
key_phrases(analyisReformedForKeyPhases)
