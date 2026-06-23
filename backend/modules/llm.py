import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings

load_dotenv()


def get_embeddings():
    """Returns Mistral's embedding model, used for both indexing and querying."""
    return MistralAIEmbeddings()


def get_llm():
    """Returns the Mistral chat model used to generate answers."""
    if not os.getenv("MISTRAL_API_KEY"):
        raise ValueError("MISTRAL_API_KEY not found in environment variables")
    return ChatMistralAI(model="mistral-small-2506")
