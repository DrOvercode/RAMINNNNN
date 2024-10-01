import streamlit as st
import requests
import json
import numpy as np

# Create a Streamlit app
st.title("Aerospace Engineer API")

# Create a text input for the user's question
prompt = st.text_input("Your question to Mr Armstrong: ")

# API endpoint URL
url = "http://localhost:11434/api/generate"

# API headers
headers = {"Content-Type": "application/json"}

# API data
data = {"model": "ALIENTELLIGENCE/aerospaceengineer", "prompt": prompt, "stream": False}

# Create a button to send the request
if st.button("Send"):
    # Send the request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the response status code
    if response.status_code == 200:
        # Parse the response text
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        st.write("Response:", actual_response)
    else:
        st.write("Error:", response.status_code, response.text)

