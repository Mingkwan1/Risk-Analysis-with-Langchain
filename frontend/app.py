import streamlit as st
import requests

# FastAPI backend URL
BACKEND_URL = "http://backend:8000"

st.title("LLM Chat Interface for Risk Analysis")

# Input for user query
query = st.text_input("Enter your question:")

if st.button("Ask"):
    if query:
        # Send the query to the FastAPI backend
        response = requests.post(f"{BACKEND_URL}/ask", json={"query": query})
        if response.status_code == 200:
            # answer = response.json().get("answer", "No answer found.")
            st.write(response.json())
        else:
            st.error("Failed to get a response from the server.")
    else:
        st.warning("Please enter a question.")