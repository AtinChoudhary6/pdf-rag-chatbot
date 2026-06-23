import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from modules.llm import get_embeddings

CHROMA_DIR = "chroma_db"


def build_vectorstore_from_pdf(file_path: str):
    """Load a single PDF, split it, embed it, and persist to chroma_db."""
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = get_embeddings()
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )
    vectorstore.persist()
    return vectorstore


def get_vectorstore():
    """Loads the existing chroma_db, or returns None if it doesn't exist yet."""
    if not os.path.exists(CHROMA_DIR):
        return None
    embeddings = get_embeddings()
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
