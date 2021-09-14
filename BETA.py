import streamlit as st

def app():
    st.info("รวมAPIเบื้องต้นสำหรับwebsiteอย่างง่าย By Ake")
    with st.echo(code_location='below'):
        st.title("This is Title")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.header("This is Header")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):  
        st.subheader("This is Subheader")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.text("This is Text")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.write("This is Write")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.markdown("This is Markdown")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.caption("This is Caption")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.image("./000003.jpg",caption="This is Image With Caption")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.audio("./000003.mp3")
    st.caption("Audio Player")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.video("./000003.mp4")
    st.caption("Video Player")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.button("This is Button")
    st.text("")
    st.text("")
    with st.echo(code_location='below'): 
        st.checkbox("This is Checkbox",value=False)
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.radio("This is Radio Button",options=['Radio Button1','Radio Button2'])
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.selectbox("This is selectbox",options=['Selectbox1','Selectbox2'])
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.slider("This is Slider")
    
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.text_input("This is Text Input")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.number_input("This is NumberInput")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.text_area("This is Text Input(>1 Lines)")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.time_input("This is TimeInput")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.date_input("This is DateInput")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.color_picker("This is ColorPicker")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.progress(50)
    st.caption("This is Progressbar") 
    st.text("") 
    st.text("")  
    with st.echo(code_location='below'):
        a = st.button("Click me For Balloons")
        
        if a:
            st.balloons()
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.error("This is Error Message")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.warning("This is Warning Message")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.info("This is Info Message")
    st.text("")
    st.text("")
    with st.echo(code_location='below'):
        st.success("This is Success Message")
    
 
