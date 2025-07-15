from fastapi import APIRouter
from .lighthouse_utils import run_lighthouse

router = APIRouter()

@router.get("/seo-audit")
def seo_audit(url: str):
    """
    Runs a Lighthouse SEO audit on the provided URL.

    Parameters:
        url (str): Website URL to audit.

    Returns:
        dict: Parsed Lighthouse audit results or error message.
    """
    result = run_lighthouse(url)
    return result
