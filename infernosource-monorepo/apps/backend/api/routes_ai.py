# apps/backend/api/routes_ai.py

from fastapi import APIRouter, HTTPException
from apps.backend.ai_rewriting.rewriting import rewrite_text
from apps.backend.database import SessionLocal
from apps.backend.scraping.models import ScrapedPage
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/rewrite-page/{page_id}")
def rewrite_page(page_id: int, style: str = "Clear, friendly marketing tone"):
    db: Session = SessionLocal()
    page = db.query(ScrapedPage).filter(ScrapedPage.id == page_id).first()

    if not page:
        db.close()
        raise HTTPException(status_code=404, detail="Page not found")

    rewritten = rewrite_text(page.extracted_text or page.html_content, style=style)

    # Store the rewritten content in extracted_text for now
    page.extracted_text = rewritten
    db.commit()
    db.refresh(page)
    db.close()

    return {"page_id": page_id, "rewritten_content": rewritten}
