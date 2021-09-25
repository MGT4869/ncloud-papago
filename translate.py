import os
import json
import urllib.request

from dotenv import load_dotenv

load_dotenv()

URL = 'https://naveropenapi.apigw.ntruss.com/nmt/v1/translation'
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def translate(text, source='ko', target='en'):
    text = urllib.parse.quote(text)
    data = f'source={source}&target={target}&text={text}'

    request = urllib.request.Request(URL)
    request.add_header("X-NCP-APIGW-API-KEY-ID",CLIENT_ID)
    request.add_header("X-NCP-APIGW-API-KEY",CLIENT_SECRET)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        response = json.loads(response_body.decode('utf-8'))
        result = response['message']['result']['translatedText']
        return result
    else:
        return "Error Code:" + rescode
