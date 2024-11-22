import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()
google_api_key= os.getenv('GOOGLE_API_KEY')

if google_api_key is None:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")

# Configure the genai client
genai.configure(api_key=google_api_key)

""" model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

response = chat.send_message("Which is one of the best place to visit in India during summer?")
print(response.text)
response = chat.send_message("Tell me more about that place in 50 words")
print(response.text)
print(chat.history) """
llm= ChatGoogleGenerativeAI(model="gemini-1.5-flash")
batch_responses = llm.batch(
    [
        "Who is the Prime Minister of India?",
        "What is the capital of India?",
    ]
)
for response in batch_responses:
    print(response.content)