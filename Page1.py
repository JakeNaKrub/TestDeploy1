import streamlit as st
import BETA
from PIL import Image
@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def loadpic(path):
    img = Image.open(path)
    return img
 
    st.title("Akeprapu's Portfolio")
    st.text("Created 08/09/2021 17:16 Made With Streamlit")
    img = loadpic("./000003.jpg")
    st.image(img,caption="Akeprapu M4")


