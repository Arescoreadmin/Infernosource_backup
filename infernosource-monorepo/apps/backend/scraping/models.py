from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from apps.backend.database import Base


class ScrapedPage(Base):
    __tablename__ = "scraped_pages"
    __table_args__ = {'extend_existing': True}  # Prevents duplicate table error on hot reload

    id = Column(Integer, primary_key=True, index=True)
    site_id = Column(Integer, ForeignKey("sites.id"), nullable=True)
    url = Column(String, index=True, nullable=True)
    html_content = Column(Text, nullable=True)
    extracted_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    site = relationship("Site", back_populates="scraped_pages")
