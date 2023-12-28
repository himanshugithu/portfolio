import streamlit as st
from send_email import send_email
st.header("contact Me")
with st.form(key="email_form"):
    user_email = st.text_input("Email address")
    raw_messege = st.text_area("Yout message")
  
    messege = f"""\
Subject:New email from {user_email}

From : {user_email}
{raw_messege}
""" 
    button = st.form_submit_button("Submit")
    if button:
        send_email(messege)
        st.info("email send successfully.....")
        
