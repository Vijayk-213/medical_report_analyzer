import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
# YOUR_GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=YOUR_GEMINI_API_KEY)

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def analyze_report_with_gemini(text):
    prompt = f"""
You are a medical expert AI.
Analyze the following medical report text:
{text}

1. Summarize the patient's condition.
2. List all diagnosis and medications.
3. Extract any vitals or measurements.
4. Provide follow-up suggestions or questions.

Format the response using markdown.
"""

    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text
