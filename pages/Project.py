import streamlit as st
import pandas as pd

hex_color_code = "#909497" 
title_text = "Projects"
styled_title = f"<h1 style='color: {hex_color_code};'>{title_text}</h1>"
st.markdown(styled_title, unsafe_allow_html=True)



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




