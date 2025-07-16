# apps/backend/scripts/seed_dummy_pages.py

from apps.backend.database import SessionLocal
from apps.backend.scraping.models import ScrapedPage

print("🔥 Seeding dummy scraped pages...")

db = SessionLocal()

dummy_pages = [
    {
        "site_id": None,
        "url": "https://example.com",
        "html_content": "<html><head><title>Example Domain</title></head><body><h1>Example</h1></body></html>",
        "extracted_text": "This domain is for use in illustrative examples.",
    },
    {
        "site_id": None,
        "url": "https://testsite.com",
        "html_content": "<html><head><title>Test Site</title></head><body><h1>Test</h1></body></html>",
        "extracted_text": "This is test content scraped from a test site.",
    },
]

for page_data in dummy_pages:
    page = ScrapedPage(**page_data)
    db.add(page)

db.commit()
db.close()

print("✅ Dummy data seeded successfully.")
