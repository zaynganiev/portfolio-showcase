import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2) 

with col1:
    st.image("images/photo.jpeg", width=750)

with col2:
    st.title("Zayn Ganiev")
    content = """
    Hi, I am Zayn Ganiev! I am a software engineer with a passion for building innovative solutions. 
    Currently, I am a freelancer online, where I focus on developing scalable applications.
    I have a strong background in algorithms and mathematics, which helps me solve complex problems efficiently.
    I am also an active participant in competitive programming contests, where I enjoy tackling challenging problems.
    """
    st.info(content)

content2 = """
    Below you can find some of the apps I have built in Python. Feel free to contact me if you have any questions or if you would like to collaborate!
    """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
