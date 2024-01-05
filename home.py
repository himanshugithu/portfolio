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
    st.info(content)


col3,col4= st.columns([1,1])
df = pd.read_csv("myself.csv",sep=";")
skill = pd.read_csv("skill.csv",sep=";")
unicode = ['\u2022','\u2713']#bullet ,checkmark
with col3:
    st.markdown(f"""<h4>{unicode[1]} Technical Skills</h4>""",unsafe_allow_html=True)
    for index, row in skill.iterrows():
       st.markdown(f"""<h7 class = space> {unicode[0]} {row[ "skill"]}</h5>""",unsafe_allow_html=True)
    

    st.markdown(f"""<h4>{unicode[1]} language </h4>""",unsafe_allow_html=True)
    lang = """
    <ul class = space>
        <li>Marathi </li> 
        <li>English </li>
        <li>Hindi </li>
    </ul>
    """
    st.markdown(lang, unsafe_allow_html=True)







with col4:
    st.markdown("<h4>Education</h4>",unsafe_allow_html=True)
    for index, row in df.iterrows():
        st.markdown(f"""
            <h5>{unicode[0]}{row["collage"]}</h5>
            <p><strong>Degree: </strong> {row["degree"]}</p>
            <p><strong>percentage: </strong>{row["percentage"]}</p>
            <p><strong>Year: </strong>{row["year"]}</p>
            <br></br>
        """, unsafe_allow_html=True)






    
st.markdown(
    """
    <style>
        body {
            line-height: 0.5;
            text-align: left;
        }
    .space {
        line-height: 1.2;  /* Adjust the value to increase or decrease line space */
    </style>
    """,
    unsafe_allow_html=True,
)   







