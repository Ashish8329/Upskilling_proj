import streamlit as st 
from pypdf import PdfReader

st.set_page_config(
    page_title="pdf chatbot",
    page_icon='📄'
)

st.title("📄 chat with your PDF")

uploaded_file = st.file_uploader('upload a pdf', type=['pdf'])

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ''

    for page in reader.pages:
        text += page.extract_text() + "\n"

    st.success('pdf loaded successfully')

    st.subheader('Extracted Text')

    st.text_area(
        'content ',
        text,
        height=300
    )

    # st.success(f'uploaded : {uploaded_file.name}')
