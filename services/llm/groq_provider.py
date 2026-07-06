# services/llm/groq_provider.py


import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv


load_dotenv()



def get_groq_key():

    key = os.getenv("GROQ_API_KEY")

    if key:
        return key


    try:
        return st.secrets["GROQ_API_KEY"]

    except Exception:

        return None





class GroqProvider:


    def __init__(self):

        api_key = get_groq_key()


        if not api_key:
            raise Exception(
                "GROQ_API_KEY missing"
            )


        self.client = Groq(
            api_key=api_key
        )




    def generate(self, prompt):


        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ],

            temperature=0.2
        )


        return response.choices[0].message.content