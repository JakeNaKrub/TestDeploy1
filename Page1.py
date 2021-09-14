import streamlit as st
from PIL import Image
 
def app():
    img = Image.open("./000003.JPG")
    st.title("Akeprapu's Portfolio")
    st.text("Created 08/09/2021 17:16 Made With Streamlit")

    #st.image(img,caption="Akeprapu M4")
