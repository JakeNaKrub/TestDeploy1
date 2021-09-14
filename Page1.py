import streamlit as st
from PIL import Image
@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def loadpic(path):
    st.image(path,caption="Akeprapu M4")
 
 
def app():
    
    st.title("Akeprapu's Portfolio")
    st.text("Created 08/09/2021 17:16 Made With Streamlit")
    img = loadpic("./000003.JPG")
 


