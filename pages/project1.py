import streamlit as st
import pandas as pd

hex_color_code = "#909497" 
title_text = "Projects"
styled_title = f"<h1 style='color: {hex_color_code};'>{title_text}</h1>"
st.markdown(styled_title, unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["♾ Arduino", "🚀ESP8266/32", "🐍Python"])
project = pd.read_csv('project.csv',sep=";")
arduino_projects = project[project['category'] == 'Arduino']
esp_projects = project[project['category'] == 'esp']
python_projects = project[project['category'] == 'python']

with tab1:
   st.header("Arduino")
   for index, row in arduino_projects.iterrows():
      st.markdown(f"""<h4>{index+1}.{row["project_name"]}</h4>""", unsafe_allow_html=True)
      st.image("image/"+ row["image"])
      st.write(f"[source code]({row["link"]})")
      st.write(f"[Video]({row["video"]})")
      with st.expander("Description"):
         st.write(row["description"])
      st.markdown("""---""")   
        
with tab2:
   st.header("Comming soon.....")
   # for index, row in esp_projects.iterrows():
   #    st.header(row["project_name"])
   #    st.image("image/"+ row["image"])
   #    st.write(f"[source code]({row["link"]})")
   #    with st.expander("Description"):
   #       st.write(row["description"])
   #    st.markdown("""---""")  

with tab3:
   st.header("Python")
   for index, row in python_projects.iterrows():
      st.header(row["project_name"])
      st.image("image/"+ row["image"])
      st.write(f"[source code]({row["link"]})")
      st.write(f"[Video]({row["video"]})")
      with st.expander("Description"):
         st.write(row["description"])
      st.markdown("""---""")   
 
