import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

st.title("Gemini GPT")

load_dotenv()
google_api_key= os.getenv('GOOGLE_API_KEY')

if google_api_key is None:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")

# Configure the genai client
genai.configure(api_key=google_api_key)

model= genai.GenerativeModel('gemini-1.5-flash')

#start the chat history
if "message" not in st.session_state:
    st.session_state.messages= [
        {
            "role": "assistant",
            "content": "Ask Me Anything"
        }
    ]
#display the messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#process the responses
def llm_function(quiery):
    response= model.generate_content(quiery)
    #display the assistant message
    with st.chat_message("assistant"):
        st.markdown(response.text)

    #store the user messages
    st.session_state.messages.append(
        {
            "rate": "user",
            "content": quiery
        }
    )
    #store the user messages
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )

#user input
quiery= st.chat_input("Hello there!")

#call the function when input is given
if quiery:
    with st.chat_message("user"):
        st.markdown(quiery)
    llm_function(quiery)