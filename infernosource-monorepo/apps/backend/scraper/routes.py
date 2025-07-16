from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from apps.backend.database import get_db
from apps.backend.crud import create_scraped_page
from apps.backend.schemas import ScrapeRequest, ScrapedPageResponse

router = APIRouter()

@router.get("/test", tags=["Scraper"])
def scraper_test():
    """Check scraper module status."""
    return {"status": "scraper route active"}

@router.post("/scrape-url", response_model=ScrapedPageResponse)
def scrape_url(request: ScrapeRequest, db: Session = Depends(get_db)):
    """
    Simulate scraping and saving the content of a webpage.
    (This is placeholder logic — replace with real scraping.)
    """
    if not request.url:
        raise HTTPException(status_code=400, detail="URL is required")
    
    # Dummy HTML & text content
    dummy_html = f"<html><body><h1>Scraped from {request.url}</h1></body></html>"
    dummy_text = f"Text extracted from {request.url}"

    # Save to DB
    scraped_page = create_scraped_page(
        db=db,
        url=request.url,
        html_content=dummy_html,
        extracted_text=dummy_text,
        site_id=request.site_id
    )
    return scraped_page
