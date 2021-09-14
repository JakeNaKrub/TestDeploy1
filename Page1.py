import streamlit as st
from PIL import Image
@st.cache(suppress_st_warning=True)
def loadpic():
    img = Image.open("./000003.JPG")
    return img
 
def app():
    
    st.title("Akeprapu's Portfolio")
    st.text("Created 08/09/2021 17:16 Made With Streamlit")
    img = loadpic()
    st.image(img,caption="Akeprapu M4")


