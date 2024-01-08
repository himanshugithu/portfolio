import streamlit as st

# Read the content of the HTML file
with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Display the HTML content
st.markdown(html_content, unsafe_allow_html=True)
