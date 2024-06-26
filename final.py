from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import requests
import os
from transformers import pipeline


load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def img2txt(url):

    imagetotext = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

    text = str(imagetotext(url))

    print(text)
    return text

def text2story(story):
    API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    template = "You are a story teller; Generate a short story on "
    finaltemplate = ''.join([template, story])

    payloads = {
        "inputs": finaltemplate
    }
    response = requests.post(API_URL, headers=headers, json=payloads)

    print(response.content)
    return response.content

def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payloads= {
        "inputs": message
    }
    response = requests.post(API_URL, headers=headers, json=payloads)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)



bro = img2txt("okakbro.jpg")
text2story(bro)



