# backend/api/routes.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/test", tags=["API"])
def api_root_test():
    """Test the central API router."""
    return {"status": "api routes active"}

@router.get("/hello", tags=["API"])
def say_hello(name: str = "InfernoSource"):
    """Returns a hello message."""
    return {"message": f"Hello, {name}!"}
