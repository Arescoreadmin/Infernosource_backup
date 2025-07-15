# apps/backend/api/routes_scraping.py

from fastapi import APIRouter, HTTPException
from apps.backend.tasks import competitor_clone_task, scrape_site_task
from apps.backend.database import SessionLocal
from apps.backend.scraping.models import ScrapedPage

router = APIRouter()

# 🚀 Route: Background competitor cloning via Celery
@router.post("/api/competitor-clone")
def clone_competitor_site(url: str):
    task = competitor_clone_task.delay(url)
    return {"task_id": task.id, "status": "Task sent to Celery"}

# 🚀 Route: Direct scraping (without Celery, synchronous)
@router.post("/api/scrape-site")
def scrape_site_direct(url: str):
    from apps.backend.scraper import scrape_site  # Local import to avoid circular issues
    result = scrape_site(url)
    return {"status": "completed", "pages": result}

# 🚀 Route: Get all scraped pages from DB
@router.get("/api/scraped-pages")
def get_scraped_pages():
    db = SessionLocal()
    pages = db.query(ScrapedPage).all()
    db.close()

    return [
        {
            "id": page.id,
            "url": page.url,
            "created_at": page.created_at.isoformat(),
            "extracted_text": page.extracted_text
        }
        for page in pages
    ]

# 🚀 Route: Get single scraped page by ID
@router.get("/api/scraped-pages/{page_id}")
def get_scraped_page(page_id: int):
    db = SessionLocal()
    page = db.query(ScrapedPage).filter(ScrapedPage.id == page_id).first()
    db.close()

    if not page:
        raise HTTPException(status_code=404, detail="Scraped page not found")

    return {
        "id": page.id,
        "url": page.url,
        "html_content": page.html_content,
        "extracted_text": page.extracted_text,
        "created_at": page.created_at.isoformat()
    }
