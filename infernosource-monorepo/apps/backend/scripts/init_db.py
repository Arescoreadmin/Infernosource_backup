# apps/backend/scripts/init_db.py

from apps.backend.database import engine
from apps.backend.scraping import models  # Import all models here!

print("🔥 Creating database tables...")
models.Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")
