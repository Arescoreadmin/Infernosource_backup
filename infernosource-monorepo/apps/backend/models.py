from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from apps.backend.database import Base

# --- Scraped Page Model ---

class ScrapedPage(Base):
    __tablename__ = "scraped_pages"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    html_content = Column(Text)
    extracted_text = Column(Text)
    site_id = Column(Integer, nullable=True)

# --- Association Table for Many-to-Many (Campaign <> ScrapedPage) ---

campaign_pages = Table(
    "campaign_pages",
    Base.metadata,
    Column("campaign_id", Integer, ForeignKey("campaigns.id"), primary_key=True),
    Column("page_id", Integer, ForeignKey("scraped_pages.id"), primary_key=True),
)

# --- Campaign Model ---

class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    pages = relationship(
        "ScrapedPage",
        secondary=campaign_pages,
        back_populates="campaigns",
        cascade="all"
    )

# Add reverse relation on ScrapedPage
ScrapedPage.campaigns = relationship(
    "Campaign",
    secondary=campaign_pages,
    back_populates="pages",
    cascade="all"
)
