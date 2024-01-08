import streamlit as st
import pandas as pd

unicode = ['\u2022','\u2713']#bullet ,checkmark
st.set_page_config(layout='wide') 
col1, col2,dumy = st.columns([0.5,0.5,0.5])
with col1 :
    st.image('image/himanshu.png',width=250)

with col2:
    st.title("Himanshu Fanibhare")    
    content="""Hello,
               My name is himanshu 
               and currently pursuing Btech
               from the st vincent pallotti collage"""  
    st.info(content)


df = pd.read_csv("myself.csv",sep=";")
skill = pd.read_csv("skill.csv",sep=";")
activity = pd.read_csv("activity.csv",sep=";")
col3,col4= st.columns([1,1])
with col3:
#----------------------------technical skills--------------------------    
    st.markdown(f"""<h4>{unicode[1]} Technical Skills</h4>""",unsafe_allow_html=True)
    for index, row in skill.iterrows():
       st.markdown(f"""<h7 class = space> {unicode[0]} {row[ "skill"]}</h5>""",unsafe_allow_html=True)

#----------------------------language--------------------------    
    st.markdown(f"""<h4>{unicode[1]} language </h4>""",unsafe_allow_html=True)
    lang = """
    <ul class = space>
        <li>Marathi </li> 
        <li>English </li>
        <li>Hindi </li>
    </ul>
    """
    st.markdown(lang, unsafe_allow_html=True)

#----------------------------web link--------------------------
    st.markdown(f"""<h4>{unicode[1]} Web links </h4>""",unsafe_allow_html=True)
    st.write(f"[Github]({"https://github.com/himanshugithu?tab=repositories"})")
    st.write(f"[Linkdin]({"https://www.linkedin.com/in/himanshu-fanibhare-11718b2a8/"})")
    st.write(f"[Instagram - The_electrogenic]({"https://www.instagram.com/the_electrogenic/"})")

#--------------------------co curricular activities-------------------------------------
    st.markdown(f"""<h4>{unicode[1]} Extra curricular </h4>""",unsafe_allow_html=True)
    for index, row in activity.iterrows():
       st.markdown(f"""<h7 class = space> {unicode[0]} {row["activity"]}</h5>""",unsafe_allow_html=True)


with col4:
    st.markdown(f"<h4>{unicode[1]}Education</h4>",unsafe_allow_html=True)
    for index, row in df.iterrows():
        st.markdown(f"""
            <h5>{unicode[0]}{row["collage"]}</h5>
            <p><strong>Degree: </strong> {row["degree"]}</p>
            <p><strong>percentage: </strong>{row["percentage"]}</p>
            <p><strong>Year: </strong>{row["year"]}</p>
            <br></br>
        """, unsafe_allow_html=True)

    st.markdown(f"<h4>{unicode[1]}Participation</h4>",unsafe_allow_html=True)
    achivements = """
    <ul class = space>
        <li>Secured first prize in a project competition entitled "Automatic
        Street Light Monitor System”.</li> 
        
    </ul>
    """
    st.markdown(achivements, unsafe_allow_html=True)

st.markdown(
    """
    <style>
        body {
            line-height: 0.5;
            text-align: left;
        }
    .space {
        line-height: 1.2;  

    .circular-image {
                border-radius: 50%;
                overflow: hidden;
            }    
    </style>
    """,
    unsafe_allow_html=True)   







