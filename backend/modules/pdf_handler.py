from pathlib import Path
from fastapi import UploadFile

UPLOAD_DIR = Path("uploaded_docs")
UPLOAD_DIR.mkdir(exist_ok=True)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


async def save_uploaded_pdf(file: UploadFile) -> str:
    """
    Validates and saves a single uploaded PDF to the uploaded_docs/ folder.
    Returns the saved file path.
    """
    if not file.filename.lower().endswith(".pdf"):
        raise ValueError(f"{file.filename} is not a PDF file")

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise ValueError(f"{file.filename} exceeds the size limit")

    # Strip any directory parts to prevent path traversal attacks
    safe_name = Path(file.filename).name
    destination = UPLOAD_DIR / safe_name
    with destination.open("wb") as buffer:
        buffer.write(contents)

    return str(destination)
