from fastapi import APIRouter, HTTPException
from apps.backend.schemas import RewriteRequest, RewriteResponse

router = APIRouter()

@router.get("/test", tags=["AI Rewriting"])
def ai_rewriting_test():
    """Check AI rewriting module status."""
    return {"status": "ai rewriting route active"}

@router.post("/rewrite-text", response_model=RewriteResponse)
def rewrite_text(request: RewriteRequest):
    """
    Dummy AI rewriting logic (replace with actual AI integration later).
    Accepts either text or a URL (but requires at least one).
    """
    if not request.text and not request.url:
        raise HTTPException(status_code=400, detail="Either text or URL is required.")

    # For now, just return a "rewritten" version (mock logic)
    input_text = request.text or f"Content fetched from {request.url}"
    rewritten = f"🔥 REWRITTEN: {input_text} 🔥"
    return RewriteResponse(rewritten_text=rewritten)
