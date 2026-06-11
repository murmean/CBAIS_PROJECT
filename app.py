import os
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
key = os.getenv("AZURE_OPENAI_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")


client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=key,
    api_version="2024-02-15-preview"
)

st.title("Real-Time Spam Detection System with Azure AI")
st.write("Enter a message and Azure AI will classify it as SPAM or NOT SPAM.")

message = st.text_area("Message:")

if st.button("Detect Spam"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {
                    "role": "system",
                    "content": "You are a spam detection system. Classify the user message only as SPAM or NOT SPAM. Add one short reason."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            temperature=0
        )

        result = response.choices[0].message.content
        st.success(result)