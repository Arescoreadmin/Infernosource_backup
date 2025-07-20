# backend/scripts/seed_db.py

import sys
import os

# Adjust the path as needed for your monorepo structure
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apps.backend.database import SessionLocal
from apps.backend.models import User, Site

def seed():
    db = SessionLocal()
    try:
        # Add a test site
        site = Site(domain="example.com")
        db.add(site)
        db.commit()
        db.refresh(site)

        # Add a test user
        user = User(email="admin@example.com", hashed_password="testhashed", full_name="Admin", role="admin")
        db.add(user)
        db.commit()
        db.refresh(user)

        print(f"Seeded site: {site.domain} (id={site.id})")
        print(f"Seeded user: {user.email} (id={user.id})")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
