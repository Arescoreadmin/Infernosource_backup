from sqlalchemy.orm import Session
from apps.backend.models import ScrapedPage, Campaign

# --- ScrapedPage CRUD ---

def create_scraped_page(db: Session, url: str, html_content: str, extracted_text: str, site_id: int = None):
    scraped_page = ScrapedPage(
        url=url,
        html_content=html_content,
        extracted_text=extracted_text,
        site_id=site_id
    )
    db.add(scraped_page)
    db.commit()
    db.refresh(scraped_page)
    return scraped_page

def get_all_scraped_pages(db: Session):
    return db.query(ScrapedPage).all()

def get_scraped_page(db: Session, page_id: int):
    return db.query(ScrapedPage).filter(ScrapedPage.id == page_id).first()

def update_scraped_page(db: Session, page_id: int, url: str = None):
    page = get_scraped_page(db, page_id)
    if not page:
        return None
    if url:
        page.url = url
    db.commit()
    db.refresh(page)
    return page

def delete_scraped_page(db: Session, page_id: int):
    page = get_scraped_page(db, page_id)
    if not page:
        return False
    db.delete(page)
    db.commit()
    return True

# --- Campaign CRUD ---

def create_campaign(db: Session, name: str, description: str = None, page_ids: list = []):
    campaign = Campaign(name=name, description=description)
    if page_ids:
        pages = db.query(ScrapedPage).filter(ScrapedPage.id.in_(page_ids)).all()
        campaign.pages = pages
    db.add(campaign)
    db.commit()
    db.refresh(campaign)
    return campaign

def get_campaigns(db: Session):
    return db.query(Campaign).all()

def get_campaign(db: Session, campaign_id: int):
    return db.query(Campaign).filter(Campaign.id == campaign_id).first()
