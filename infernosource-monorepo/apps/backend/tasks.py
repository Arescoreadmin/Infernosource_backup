# apps/backend/tasks.py

from apps.backend.celery_worker import celery
from apps.backend.scraper import scrape_site
from apps.backend.ai_rewriting.rewriting import rewrite_text
from apps.backend.database import SessionLocal
from apps.backend.scraping.models import ScrapedPage

@celery.task
def scrape_site_task(url: str):
    """
    Example Celery task to scrape a site synchronously.
    """
    return scrape_site(url)

@celery.task
def competitor_clone_task(url: str, rewrite_style: str = "Clear, friendly marketing tone"):
    """
    Full pipeline:
    1. Scrape competitor site
    2. Store pages in DB
    3. Rewrite content via OpenAI
    4. Update DB with rewritten text
    """
    # Step 1: Scrape site
    scraped_pages = scrape_site(url)
    
    # Step 2: Store raw pages and rewritten versions in DB
    db = SessionLocal()
    for page in scraped_pages:
        # Store original
        scraped_page = ScrapedPage(
            url=page["url"],
            html_content=page["html"],
            extracted_text=None  # Placeholder until rewritten
        )
        db.add(scraped_page)
        db.commit()
        db.refresh(scraped_page)

        # Step 3: Rewrite content via OpenAI
        rewritten = rewrite_text(page["html"], style=rewrite_style)

        # Step 4: Update record with rewritten text
        scraped_page.extracted_text = rewritten
        db.commit()
    db.close()

    return {"status": "completed", "pages_processed": len(scraped_pages)}
