import os
import streamlit as st
import openai
from dotenv import load_dotenv

load_dotenv()

# streamlit run quickchat_azure_openai.py

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_BASE")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_version = "2023-03-15-preview"

st.title('🦜🔗 Quickstart App')

def generate_response(input_text):
    response = openai.ChatCompletion.create(
        engine="Gpt35Turbo16k",
        messages = [
            {"role":"system","content":"You are an AI assistant that helps people find information."},
            {"role": "user", "content": input_text}],
        temperature=0.7,
        max_tokens=2000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    result = ''
    for choice in response.choices:
        result += choice.message.content

    st.info(result)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)
