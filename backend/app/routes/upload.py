from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from app.services.hash_service import calculate_sha256

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload", tags=["Evidence"])
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    # Simpan file
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Hitung SHA256
    sha256 = calculate_sha256(file_path)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_path": str(file_path),
        "sha256": sha256,
        "status": "uploaded_and_verified"
    }