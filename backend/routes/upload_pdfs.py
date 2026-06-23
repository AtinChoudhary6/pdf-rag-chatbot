from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from modules.pdf_handler import save_uploaded_pdf
from modules.load_vectorstore import build_vectorstore_from_pdf
from middleware.auth import verify_api_key
from logger import logger

router = APIRouter()


@router.post("/upload-pdf/", dependencies=[Depends(verify_api_key)])
async def upload_pdf(file: UploadFile = File(...)):
    """
    Accepts a single PDF file, saves it to disk, then builds/persists
    the chroma_db vectorstore from it.
    """
    try:
        saved_path = await save_uploaded_pdf(file)
        build_vectorstore_from_pdf(saved_path)
        logger.info(f"Uploaded and indexed: {saved_path}")
        return {"message": "Vector DB created successfully", "file": saved_path}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Upload failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to process PDF")
