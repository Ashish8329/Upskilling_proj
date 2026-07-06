import streamlit as st 

st.set_page_config(
    page_title="pdf chatbot",
    page_icon='📄'
)

st.title("📄 chat with your PDF")

uploaded_file = st.file_uploader('upload a pdf', type=['pdf'])

if uploaded_file:
    st.success(f'uploaded : {uploaded_file.name}')