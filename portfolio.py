import streamlit as st
# st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1 :
    st.image('image/himanshu.jpg',width=300)

with col2:
    st.title("Himanshu Fanibhare")    
    content="""Hello,
               My name is himanshu 
               and current pursuing Btech
               from the st vincent pallotti collage"""
    # st.write(content) 
    st.info(content)
content2 = """My Projects"""
st.write(content2)