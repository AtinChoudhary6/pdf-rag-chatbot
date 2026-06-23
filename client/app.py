import streamlit as st
from components.upload import render_uploader
from components.chatUI import render_chat

st.set_page_config(page_title="PDF RAG Chatbot")
st.title("📚 PDF RAG Chatbot")
st.write("Upload any PDF and ask questions about its content")

render_uploader()
render_chat()
