import streamlit as st
from PIL import Image
@st.cache(suppress_st_warning=True)
def loadpic():
    global img
    img = Image.open("./000003.JPG")
def app():
    
    st.title("Akeprapu's Portfolio")
    st.text("Created 08/09/2021 17:16 Made With Streamlit")

    st.image(img,caption="Akeprapu M4")
loadpic()
app()
