from sites.models import Page
from database import SessionLocal

db = SessionLocal()

# Add sample pages
db.add(Page(title="Welcome to InfernoSource"))
db.add(Page(title="About This Project"))
db.commit()

print("Sample pages added!")
