from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from apps.backend.database import get_db
from apps.backend.schemas import RewriteRequest, RewriteResponse
from apps.backend.ai_rewriting.rewriting import rewrite_text

router = APIRouter()

@router.get("/test", tags=["AI Rewriting"])
def rewrite_test():
    """Check AI rewriting module status."""
    return {"status": "ai_rewriting route active"}

@router.post("/rewrite", response_model=RewriteResponse)
def rewrite_endpoint(request: RewriteRequest, db: Session = Depends(get_db)):
    """
    Rewrite given text using the AI model.
    """
    if not request.text:
        raise HTTPException(status_code=400, detail="Text to rewrite is required")
    
    rewritten = rewrite_text(request.text, tone=request.tone)
    return {"original": request.text, "rewritten": rewritten}
