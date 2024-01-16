#https://makersuite.google.com/app/apikey
#https://ai.google.dev/tutorials/python_quickstart
#pip install -q -U google-generativeai
#pip3 install Pillow
import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
#print(GEMINI_API_KEY)

#Use list_models to see the available Gemini models
"""
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
"""

img = PIL.Image.open('image.jpeg')

model = genai.GenerativeModel('gemini-pro-vision')
response1 = model.generate_content(img)
print(response1.text)
print("break1\n")

response2 = model.generate_content(["Write a short, engaging blog post based on this picture. It should include a description of the place in the photo and talk about my journey to going to the place.", img], stream=True)
response2.resolve()
print(response2.text)
print("break2\n")