from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from modules.query_handler import query_chain
from middleware.auth import verify_api_key
from logger import logger

router = APIRouter()


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=500)


@router.post("/ask/", dependencies=[Depends(verify_api_key)])
def ask_question(data: QueryRequest):
    """
    Accepts a question and returns an answer generated from the most
    relevant chunks stored in chroma_db.
    """
    try:
        result = query_chain(data.question)
        if result is None:
            raise HTTPException(status_code=400, detail="Vector DB not found. Upload a PDF first.")
        logger.info(f"Answered question: {data.question}")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Query failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to answer question")
