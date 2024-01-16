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
#Initialize the chat:
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
chat

# Prompt the user for input
user_input = input("Please enter the prompt as a chat to the model ")
# Display the entered text
print("Your prompt is:", user_input)
print("break1\n")

#send_message method returns the same GenerateContentResponse type as GenerativeModel.generate_content. It  appends your message and the response to the chat history:
response = chat.send_message(user_input)
print(response.text)
print("break2\n")
print(chat.history)
print("break3\n")

response = chat.send_message(user_input, stream=True)

for chunk in response:
  print(chunk.text)
  print("_"*80)

print("break4\n")