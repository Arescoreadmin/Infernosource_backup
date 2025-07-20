from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from apps.backend.database import get_db
from apps.backend.models import ScrapedPage
from apps.backend.schemas import (
    ScrapedPageResponse, ScrapeRequest,
    CampaignCreate, CampaignResponse
)
from apps.backend.crud import (
    create_campaign, get_campaigns, get_campaign
)

router = APIRouter()

# ----- Scraped Pages CRUD -----

@router.get("/test", tags=["Sites"])
def sites_test():
    """Check Sites route status."""
    return {"status": "sites route active"}

@router.get("/pages", response_model=List[ScrapedPageResponse], tags=["Sites"])
def list_scraped_pages(db: Session = Depends(get_db)):
    """Return all scraped pages."""
    pages = db.query(ScrapedPage).all()
    return pages

@router.get("/pages/{page_id}", response_model=ScrapedPageResponse, tags=["Sites"])
def get_scraped_page(page_id: int, db: Session = Depends(get_db)):
    """Return a single scraped page by ID."""
    page = db.query(ScrapedPage).filter(ScrapedPage.id == page_id).first()
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    return page

@router.put("/pages/{page_id}", response_model=ScrapedPageResponse, tags=["Sites"])
def update_scraped_page(page_id: int, payload: ScrapeRequest, db: Session = Depends(get_db)):
    """Update the URL of a scraped page."""
    page = db.query(ScrapedPage).filter(ScrapedPage.id == page_id).first()
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    if payload.url:
        page.url = payload.url
    # Extend this section to update more fields as needed
    db.commit()
    db.refresh(page)
    return page

@router.delete("/pages/{page_id}", tags=["Sites"])
def delete_scraped_page(page_id: int, db: Session = Depends(get_db)):
    """Delete a scraped page by ID."""
    page = db.query(ScrapedPage).filter(ScrapedPage.id == page_id).first()
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    db.delete(page)
    db.commit()
    return {"detail": "Page deleted"}

# ----- Campaign CRUD -----

@router.post("/campaigns", response_model=CampaignResponse, tags=["Campaigns"])
def create_new_campaign(payload: CampaignCreate, db: Session = Depends(get_db)):
    """Create a new campaign and link scraped pages."""
    campaign = create_campaign(
        db,
        name=payload.name,
        description=payload.description,
        page_ids=payload.page_ids or []
    )
    return CampaignResponse(
        id=campaign.id,
        name=campaign.name,
        description=campaign.description,
        page_ids=[p.id for p in campaign.pages]
    )

@router.get("/campaigns", response_model=List[CampaignResponse], tags=["Campaigns"])
def list_campaigns(db: Session = Depends(get_db)):
    """List all campaigns."""
    campaigns = get_campaigns(db)
    return [
        CampaignResponse(
            id=c.id,
            name=c.name,
            description=c.description,
            page_ids=[p.id for p in c.pages]
        ) for c in campaigns
    ]

@router.get("/campaigns/{campaign_id}", response_model=CampaignResponse, tags=["Campaigns"])
def get_campaign_details(campaign_id: int, db: Session = Depends(get_db)):
    """Get campaign details by ID."""
    campaign = get_campaign(db, campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return CampaignResponse(
        id=campaign.id,
        name=campaign.name,
        description=campaign.description,
        page_ids=[p.id for p in campaign.pages]
    )
