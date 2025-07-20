# backend/scripts/test_api.py

import requests

BASE_URL = "http://localhost:8000"

def test_health():
    print("Testing /health ...")
    r = requests.get(f"{BASE_URL}/health")
    print("Status:", r.status_code)
    print("Response:", r.json())

def test_scraper():
    print("Testing /scrape/test ...")
    r = requests.get(f"{BASE_URL}/scrape/test")
    print("Status:", r.status_code)
    print("Response:", r.json())

def test_ai_rewriting():
    print("Testing /rewrite/test ...")
    r = requests.get(f"{BASE_URL}/rewrite/test")
    print("Status:", r.status_code)
    print("Response:", r.json())

    print("Testing /rewrite/rewrite-text ...")
    data = {"text": "This is a test to rewrite.", "url": None}
    r = requests.post(f"{BASE_URL}/rewrite/rewrite-text", json=data)
    print("Status:", r.status_code)
    print("Response:", r.json())

def test_seo():
    print("Testing /seo/test ...")
    r = requests.get(f"{BASE_URL}/seo/test")
    print("Status:", r.status_code)
    print("Response:", r.json())

    print("Testing /seo/analyze ...")
    data = {"html": "<html><head><title>Test</title></head><body>Sample</body></html>"}
    r = requests.post(f"{BASE_URL}/seo/analyze", json=data)
    print("Status:", r.status_code)
    print("Response:", r.json())

if __name__ == "__main__":
    test_health()
    test_scraper()
    test_ai_rewriting()
    test_seo()
