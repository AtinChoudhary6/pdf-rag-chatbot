from langchain_core.prompts import ChatPromptTemplate
from modules.llm import get_llm
from modules.load_vectorstore import get_vectorstore

SYSTEM_PROMPT = """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""

PROMPT = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "Context:\n{context}\n\nQuestion:\n{question}\n"),
])


def get_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.5},
    )


def query_chain(question: str):
    """
    Full RAG pipeline: retrieve relevant chunks -> build prompt -> call LLM.
    Returns None if no vectorstore has been created yet.
    """
    vectorstore = get_vectorstore()
    if vectorstore is None:
        return None

    retriever = get_retriever(vectorstore)
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)

    final_prompt = PROMPT.invoke({"context": context, "question": question})

    llm = get_llm()
    response = llm.invoke(final_prompt)

    return {
        "answer": response.content,
        "sources": sorted({doc.metadata.get("source", "unknown") for doc in docs}),
    }
