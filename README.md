# 🤖 RAG Chatbot — AI-Powered Document Question Answering

A production-ready **Retrieval-Augmented Generation (RAG) Chatbot** built using **FastAPI, LangChain, ChromaDB, Mistral Embeddings, and Mistral LLM**.

The application enables users to upload PDF documents and interact with them through natural language queries. Instead of relying solely on the LLM's pre-trained knowledge, the system retrieves relevant information from uploaded documents and generates accurate, context-aware responses grounded in the document content.

---

## 🚀 Overview

Large Language Models are powerful but can hallucinate or lack knowledge about custom documents.

This project solves that problem using **Retrieval-Augmented Generation (RAG)** by combining:

* Semantic Search
* Vector Databases
* Embedding Models
* Large Language Models

Users can upload one or more PDF files, and the chatbot retrieves the most relevant document chunks before generating responses, ensuring answers are accurate, relevant, and source-aware.

---

## ✨ Features

### 📄 Intelligent PDF Processing

* Single and Multiple PDF Upload Support
* Automatic Text Extraction
* Efficient Document Chunking
* Persistent Knowledge Base

### 🔍 Semantic Search

* Mistral Embeddings for Vector Generation
* Meaning-Based Retrieval
* Contextual Document Understanding

### 🧠 Retrieval-Augmented Generation (RAG)

* Retrieves Relevant Context Before Generation
* Reduces Hallucinations
* Improves Answer Accuracy

### 💬 Interactive Chat Experience

* Streamlit-Based User Interface
* Natural Language Question Answering
* Real-Time Responses

### ⚡ FastAPI Backend

* High Performance REST APIs
* Modular Architecture
* Easy Frontend Integration

### 🗂️ Vector Database

* ChromaDB Persistent Storage
* Fast Similarity Search
* Efficient Retrieval Pipeline

### 🛡️ Production-Oriented Design

* Global Exception Handling
* Centralized Logging
* Environment-Based Configuration
* Modular Code Structure

---

## 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │   PDF Upload    │
                    └────────┬────────┘
                             │
                             ▼
                  ┌────────────────────┐
                  │ PDF Text Extraction│
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │    Text Chunking   │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Mistral Embeddings │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │      ChromaDB      │
                  └────────┬───────────┘

──────────────────────────────────────────────────

                    User Question
                           │
                           ▼
                  ┌────────────────────┐
                  │ Similarity Search  │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Relevant Chunks    │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Context Creation   │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │    Mistral LLM     │
                  └────────┬───────────┘
                           │
                           ▼
                   Generated Answer
```

---

## 🛠️ Tech Stack

| Component       | Technology         |
| --------------- | ------------------ |
| Backend         | FastAPI            |
| Frontend        | Streamlit          |
| Framework       | LangChain          |
| LLM             | Mistral Chat       |
| Embeddings      | Mistral Embeddings |
| Vector Database | ChromaDB           |
| Server          | Uvicorn            |
| Language        | Python             |

---

## 📂 Project Structure

```bash
rag-chatbot/
│
├── backend/
│   │
│   ├── main.py
│   ├── logger.py
│   │
│   ├── middleware/
│   │   ├── auth.py
│   │   ├── exception_handlers.py
│   │   └── __init__.py
│   │
│   ├── modules/
│   │   ├── llm.py
│   │   ├── load_vectorstore.py
│   │   ├── pdf_handler.py
│   │   ├── query_handler.py
│   │   └── __init__.py
│   │
│   ├── routes/
│   │   ├── ask_question.py
│   │   ├── upload_pdfs.py
│   │   └── __init__.py
│   │
│   ├── chroma_db/
│   ├── uploaded_docs/
│   └── requirements.txt
│
├── client/
│   ├── app.py
│   ├── config.py
│   ├── components/
│   ├── utils/
│   └── requirements.txt
│
├── .env
├── .gitignore
├── render.yaml
├── requirements.txt
└── README.md
```

## 🎯 Key Highlights

✅ End-to-End RAG Pipeline

✅ FastAPI + Streamlit Integration

✅ Semantic Search with Mistral Embeddings

✅ ChromaDB Persistent Vector Storage

✅ Source-Grounded Responses

✅ Modular and Scalable Architecture

✅ Logging and Exception Handling

✅ Production-Ready Project Structure


---

## 👨‍💻 Author

### Atin Choudhary


Give this repository a star and feel free to contribute or provide feedback.
