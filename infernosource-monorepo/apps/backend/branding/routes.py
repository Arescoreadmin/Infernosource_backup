from fastapi import APIRouter, File, UploadFile, Depends
from apps.backend.auth import get_current_user

router = APIRouter()

@router.post("/upload-logo")
def upload_logo(site_id: int, file: UploadFile = File(...), user=Depends(get_current_user)):
    # Save the logo file to disk (or S3, etc.)
    with open(f"logos/{site_id}_{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    # Link the logo to your Site in the DB here if needed
    return {"success": True, "filename": file.filename}
