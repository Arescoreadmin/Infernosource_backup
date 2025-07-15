# apps/backend/scraping/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from apps.backend.database import Base
from apps.backend.models import Site  # ✅ Import Site instead of redefining it

# 🚀 ScrapedPage model
class ScrapedPage(Base):
    __tablename__ = "scraped_pages"

    id = Column(Integer, primary_key=True, index=True)
    site_id = Column(Integer, ForeignKey("sites.id"), nullable=True)
    url = Column(String, index=True, nullable=True)
    html_content = Column(Text, nullable=True)
    extracted_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Site
    site = relationship("Site", back_populates="scraped_pages")
