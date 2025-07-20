from fastapi import APIRouter, HTTPException, status
from apps.backend.schemas import UserCreate, UserOut

router = APIRouter()

# Dummy user store for demonstration only!
dummy_users = {
    "demo@example.com": {
        "id": 1,
        "email": "demo@example.com",
        "full_name": "Demo User",
        "role": "user",
        "password": "demo123"  # plaintext for demo; never do this in prod!
    }
}

@router.get("/test", tags=["Auth"])
def auth_test():
    """Check Auth route status."""
    return {"status": "auth route active"}

@router.post("/register", response_model=UserOut, tags=["Auth"])
def register_user(user: UserCreate):
    """
    Register a new user (dummy logic, replace with real DB/auth system).
    """
    if user.email in dummy_users:
        raise HTTPException(status_code=400, detail="Email already registered.")
    user_id = len(dummy_users) + 1
    dummy_users[user.email] = {
        "id": user_id,
        "email": user.email,
        "full_name": None,
        "role": "user",
        "password": user.password
    }
    return UserOut(
        id=user_id,
        email=user.email,
        full_name=None,
        role="user"
    )

@router.post("/login", response_model=UserOut, tags=["Auth"])
def login_user(user: UserCreate):
    """
    Dummy login (checks hardcoded user store).
    """
    record = dummy_users.get(user.email)
    if not record or record["password"] != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password."
        )
    return UserOut(
        id=record["id"],
        email=record["email"],
        full_name=record["full_name"],
        role=record["role"]
    )
