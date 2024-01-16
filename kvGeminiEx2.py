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

#Use list_models to see the available Gemini models
"""
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
"""
#For text-only prompts, use the gemini-pro model:
model = genai.GenerativeModel('gemini-pro')

# Prompt the user for input
user_input = input("Please enter the prompt to the model ")
# Display the entered text
print("Your prompt is:", user_input)

#you can pass a prompt string to the model
response = model.generate_content(user_input)

#In simple cases, the response.text accessor is all you need. To display formatted Markdown text, use the to_markdown function:
print(response.text)
print("break1")
#If the API failed to return a result, use prompt_feedback to see if it was blocked due to saftey concerns regarding the prompt.
#print(response.prompt_feedback)
#print("break2")
print(response.candidates)
print("break3")

#stream the response as it is being generated, and the model will return chunks of the response as soon as they are generated
response = model.generate_content(user_input, stream=True)
#when streaming, some response attributes are not available until you've iterated through all the response chunks. This is demonstrated below
#print(response.text)
print("break4")
for chunk in response:
  print(chunk.text)
  print("_"*80)
