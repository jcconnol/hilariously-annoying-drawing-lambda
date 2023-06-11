import boto3
import json
from responses import response
from PIL import Image
from pytesseract import pytesseract

s3_client = boto3.client('s3', region_name='us-east-2')

REQUIRED_KEYS = ["image"]

def endpoint(event):

    eventBody = json.loads(event["body"])

    if not haveExtraKeys(eventBody) and haveRequiredKeys(eventBody):
        return response(400, "Incorrect keys provided")

    try:
        # path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        # pytesseract.tesseract_cmd = path_to_tesseract
        foundCharacter = pytesseract.image_to_string(eventBody["image"])
        return response(200, { "phrase": foundCharacter })

    except Exception as e:
        print(e)
        return response(500, e)

def haveRequiredKeys(inputObj):
    for value in REQUIRED_KEYS:
        if value not in inputObj.keys():
            return False

    return True

def haveExtraKeys(inputObj):
    for key in list(inputObj.keys()):
        print(key)
        if key not in REQUIRED_KEYS:
            print(key)
            print(REQUIRED_KEYS)
            return False

    return True
