from sqlalchemy import Column, Integer, String
from database import Base

class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
