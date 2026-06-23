import streamlit as st
from utils.api import upload_pdf_api


def render_uploader():
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file:
        st.success("PDF uploaded successfully!")

        if st.button("Create Vector Database"):
            with st.spinner("Processing document..."):
                response = upload_pdf_api(uploaded_file)
            if "message" in response:
                st.success(response["message"])
            else:
                st.error(response.get("detail", "Upload failed"))
