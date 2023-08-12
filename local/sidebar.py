import streamlit as st

def app():
    
    st.sidebar.button('Hit me')
    st.sidebar.checkbox('Check me out')
    st.sidebar.radio('Radio', [1,2,3])
    st.sidebar.selectbox('Select', [1,2,3])
    st.sidebar.multiselect('Multiselect', [1,2,3])
    st.sidebar.slider('Slide me', min_value=0, max_value=10)
    st.sidebar.select_slider('Slide to select', options=[1,'2'])
    st.sidebar.text_input('Enter some text')
    st.sidebar.number_input('Enter a number')
    st.sidebar.text_area('Area for textual entry')
    st.sidebar.date_input('Date input')
    st.sidebar.time_input('Time entry')
    st.sidebar.file_uploader('File uploader')
    st.sidebar.color_picker('Pick a color')
