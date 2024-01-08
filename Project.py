import streamlit as st
import pandas as pd

hex_color_code = "#909497" 
title_text = "Projects"
styled_title = f"<h1 style='color: {hex_color_code};'>{title_text}</h1>"
st.markdown(styled_title, unsafe_allow_html=True)

st.markdown(f"""<h5>Arduino based project</h5>""", unsafe_allow_html=True)
col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
col5,empty_col1,col6 = st.columns([1.5,0.5,1.5])

project = pd.read_csv('project.csv',sep=";")
arduino_projects = project[project['category'] == 'Arduino']
esp_projects = project[project['category'] == 'esp']
python_projects = project[project['category'] == 'python']

with col3:
    for index, row in arduino_projects[len(arduino_projects)//2:].iterrows():
        st.header(row["project_name"])
        st.write(row["category"])
    st.markdown(f"""<h5>ESP based project</h5>""", unsafe_allow_html=True)    
with col4:
    for index, row in arduino_projects[len(arduino_projects)//2:].iterrows():
        st.header(row["project_name"])
        st.write(row["category"])        



with col5:
    for index, row in esp_projects[len(esp_projects)//2:].iterrows():
        st.header(row["project_name"])
        st.write(row["category"])
with col6:
    for index, row in esp_projects[len(esp_projects)//2:].iterrows():
        st.header(row["project_name"])
        st.write(row["category"])  
