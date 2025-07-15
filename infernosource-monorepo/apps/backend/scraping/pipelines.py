# apps/backend/scraping/pipelines.py

from apps.backend.database import SessionLocal
from apps.backend.scraping.models import ScrapedPage

class SaveToDatabasePipeline:
    def process_item(self, item, spider):
        db = SessionLocal()
        page = ScrapedPage(
            url=item['url'],
            html_content=item['html'],
        )
        db.add(page)
        db.commit()
        db.close()
        return item
