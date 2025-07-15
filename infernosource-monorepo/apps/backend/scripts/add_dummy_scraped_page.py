from apps.backend.database import SessionLocal
from apps.backend.scraping.models import ScrapedPage

def main():
    db = SessionLocal()

    page = ScrapedPage(
        url="https://example.com",
        html_content="<html><body><h1>Test Page</h1></body></html>",
        extracted_text="Test Page"
    )
    db.add(page)
    db.commit()
    db.refresh(page)
    print(f"Inserted test page with ID: {page.id}")

    db.close()

if __name__ == "__main__":
    main()