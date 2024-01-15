#https://makersuite.google.com/app/apikey
#https://ai.google.dev/tutorials/python_quickstart
#pip install -q -U google-generativeai
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
#print(GEMINI_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is latest ABOUT SOLID design?")
print(response.text)