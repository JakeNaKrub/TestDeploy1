import streamlit as st
from PIL import Image
st.header("ตัวอย่างผลงาน")
clicked = st.button("Click Me!")
if clicked:
    st.info("สร้างโดยเอกปาพู")
    st.balloons()
    with st.expander("Source Code!"):
        st.write("Source Code")
        st.write("https://github.com/JakeNaKrub/TestDeploy1")