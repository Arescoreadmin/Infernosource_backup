# apps/backend/scraping/pipelines.py

from sqlalchemy.orm import sessionmaker
from apps.backend.database import SessionLocal
from apps.backend.scraping.models import ScrapedPage

class SaveToDatabasePipeline:
    def process_item(self, item, spider):
        session = SessionLocal()
        page = ScrapedPage(
            job_id=item['job_id'],
            site_id=item.get('site_id'),
            url=item['url'],
            status_code=item.get('status_code'),
            html_content=item.get('html_content'),
            extracted=item.get('extracted'),
        )
        session.add(page)
        session.commit()
        session.close()
        return item
