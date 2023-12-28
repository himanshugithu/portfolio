import streamlit as st
# wcvh dkrs okfy swom
st.header("contact Me")
with st.form(key="email_form"):
    user_email = st.text_input("Email address")
    messege = st.text_area("Yout message")
    button = st.form_submit_button("Submit")
    if button:
        print("pressed")
