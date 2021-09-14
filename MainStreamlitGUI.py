import base64
from PIL import Image
import pandas as pd
import streamlit as st
# IMPORT ALL PAGE
import Page2
import Page1
import Page3
import BETA
 
 #Path Set
#img = Image.open("D:\\Work\\000003.jpg")
###################PORTZONE
returned = 0
PAGES = {
     "ข้อมูลส่วนบุคคล": Page1,
     "ประวัติการศึกษา": Page2,
     "ตัวอย่างผลงาน": Page3,
     "ตัวอย่างAPI":BETA


}
st.sidebar.title('Menu')
menu_list = list(PAGES.keys())


selection = st.sidebar.radio("",menu_list,index=returned)
st.sidebar.warning("อาจโหลดช้าเพราะไฟล์ภาพใหญ่จ้า")
page = PAGES[selection]


 


 
