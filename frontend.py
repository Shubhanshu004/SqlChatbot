import streamlit as st
import requests

# Streamlit app title
st.title("AI-powered SQL Chatbot")

# Input fields
query = st.text_area("Enter your SQL query in natural language:")
db_user = st.text_input("Database User", "root")
db_password = st.text_input("Database Password", "12345", type="password")
db_host = st.text_input("Database Host", "localhost")
db_name = st.text_input("Database Name", "pandeyji_eatery")

# Button to send query
if st.button("Run Query"):
    if query.strip():
        # API request to Flask backend
        api_url = "http://127.0.0.1:5000/query"
        request_data = {
            "query": query,
            "db_user": db_user,
            "db_password": db_password,
            "db_host": db_host,
            "db_name": db_name
        }

        try:
            response = requests.post(api_url, json=request_data)
            if response.status_code == 200:
                st.success("Query executed successfully!")
                st.json(response.json())  # Show response as JSON
            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to backend: {e}")
    else:
        st.warning("Please enter a query before running.")

