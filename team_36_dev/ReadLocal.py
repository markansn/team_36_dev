import requests
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

import os;
import sys;

array1 = [692, 62, 17, 13]
array2 = [717,64,86,14]
limit = 20

def int_parse(array1, array2):
    for element in array1:
        element = int(element)
    for element in array2:
        element = int(element)
    return array1, array2
    
def distance(array1, array2):
    int_parse(array1, array2); 
    state = True
    x_coordinate_array1 = array1[0] + array1[2]
    y_coordinate_array1 = array1[1]

    x_coordinate_array2 = array2[0]
    y_coordinate_array2 = array2[1]
    if((x_coordinate_array2 - x_coordinate_array1) < limit):
        state = True
    elif((y_coordinate_array2 -  y_coordinate_array1) < limit):
        state = True 
    else:
        state = False
    return state

subscription_key = "ffcc4bbd174c4b6e97d0a945aebf8b98"
endpoint = "https://uksouth.api.cognitive.microsoft.com/"

def authenticateClient():
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credentials=credentials)
    return text_analytics_client


def key_phrases(doc):
    client = authenticateClient()
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

def OCR2KeyPhrasesReFormatter(OCRout):
    return 0

def ConvertToJSON(OCRout):
    temp = str(OCRout)
    temp = temp.replace('\'', '\"')
    return temp

ocr_url = endpoint + "vision/v2.1/ocr"

# Set image_path to the local path of an image that you want to analyze.
image_path = "/Users/tulmultechnologies/team_36_dev/image/text1.png"

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

#key_phrases(analysis)



