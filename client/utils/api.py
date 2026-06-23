import os
import requests
from dotenv import load_dotenv
from config import API_URL

load_dotenv()

HEADERS = {"x-api-key": os.getenv("BACKEND_API_KEY", "")}


def upload_pdf_api(file):
    """Sends the uploaded PDF (from st.file_uploader) to the backend."""
    files = {"file": (file.name, file.getvalue(), "application/pdf")}
    response = requests.post(f"{API_URL}/upload-pdf/", files=files, headers=HEADERS)
    return response.json()


def ask_question_api(question: str):
    """Sends a question to the backend and returns the JSON response."""
    response = requests.post(f"{API_URL}/ask/", json={"question": question}, headers=HEADERS)
    return response.json()
