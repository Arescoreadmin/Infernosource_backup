# apps/backend/seo_parser.py

import requests
from bs4 import BeautifulSoup

def analyze_seo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    meta = {
        meta.attrs.get('name', ''): meta.attrs.get('content', '')
        for meta in soup.find_all('meta') if 'name' in meta.attrs
    }
    return {"url": url, "meta_tags": meta}
