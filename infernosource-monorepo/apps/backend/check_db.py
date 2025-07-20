from database import SessionLocal   # No dot, just plain 'database'
from sites.models import Page

db = SessionLocal()
pages = db.query(Page).all()
for p in pages:
    print(f"{p.id}: {p.title}")
db.close()
