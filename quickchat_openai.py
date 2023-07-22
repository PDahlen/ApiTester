import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()

# streamlit run quickchat_openai.py

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title('🦜🔗 Quickstart App')

def generate_response(input_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": input_text},
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    st.info(result)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)
