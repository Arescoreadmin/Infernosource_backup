from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from apps.backend.database import Base
import enum

class ScrapeStatus(enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"

class ScrapeJob(Base):
    __tablename__ = "scrape_jobs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    site_id = Column(Integer, ForeignKey("sites.id"), nullable=False)
    status = Column(Enum(ScrapeStatus), default=ScrapeStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    log = Column(Text, nullable=True)
    pages = relationship("ScrapedPage", back_populates="job", cascade="all, delete-orphan")

class ScrapedPage(Base):
    __tablename__ = "scraped_pages"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("scrape_jobs.id"), nullable=False)
    site_id = Column(Integer, ForeignKey("sites.id"), nullable=True)
    url = Column(String, index=True, nullable=False)
    status_code = Column(Integer, nullable=True)
    html_content = Column(Text, nullable=True)
    extracted = Column(JSON, nullable=True)  # {"title": ..., "h1": [...], "images": [...], ...}
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    job = relationship("ScrapeJob", back_populates="pages")
    site = relationship("Site", back_populates="scraped_pages")
