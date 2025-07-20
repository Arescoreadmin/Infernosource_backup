# backend/utils.py

import hashlib
import random
import string

def generate_random_string(length=12):
    """Generate a random alphanumeric string."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def hash_password(password: str) -> str:
    """Return a simple hash of the password (replace with bcrypt or similar for production!)."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check if a plain password matches the hashed password."""
    return hash_password(plain_password) == hashed_password
