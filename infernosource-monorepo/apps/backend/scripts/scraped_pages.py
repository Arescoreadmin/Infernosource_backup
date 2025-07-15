# apps/backend/scripts/check_scraped_pages.py

from apps.backend.database import SessionLocal
from apps.backend.scraping.models import ScrapedPage

def main():
    db = SessionLocal()
    pages = db.query(ScrapedPage).all()
    for page in pages:
        print(f"Page ID: {page.id}, URL: {page.url}")
    db.close()

if __name__ == "__main__":
    main()
