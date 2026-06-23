import streamlit as st
from utils.api import ask_question_api


def render_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.divider()
    st.subheader("💬 Chat with your PDF")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    query = st.chat_input("Ask a question about the PDF...")

    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.write(query)

        data = ask_question_api(query)
        answer = data.get("answer", data.get("detail", "Something went wrong."))

        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)
