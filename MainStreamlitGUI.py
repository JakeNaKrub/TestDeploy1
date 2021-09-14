import base64
from PIL import Image
import pandas as pd
import streamlit as st
# IMPORT ALL PAGE
import Page2
import Page1
import Page3

#Path Set
#img = Image.open("D:\\Work\\000003.jpg")
###################PORTZONE
PAGES = {
    "A": Page1,
    "B": Page2,
    "VC": Page3,

    
}
menu_list = list(PAGES.keys())

st.sidebar.title('Menu')
 
selection = st.sidebar.radio("",menu_list)

page = PAGES[selection]
page.app()

 
 
 
