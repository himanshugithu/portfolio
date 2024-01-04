import streamlit as st
import pandas as pd

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
col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
df = pd.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:len(df)//2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/"+ row["image"])
        st.write(f"[source code]({row["url"]})")

with col4:
    for index, row in df[len(df)//2:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/"+ row["image"])
        st.write(f"[source code]({row["url"]})")