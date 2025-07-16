# apps/backend/scraping/spiders/competitor_spider.py

import scrapy
from bs4 import BeautifulSoup

class CompetitorSpider(scrapy.Spider):
    name = "competitor_spider"

    def __init__(self, start_urls=None, job_id=None, site_id=None, max_depth=2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = start_urls if isinstance(start_urls, list) else [start_urls]
        self.job_id = job_id
        self.site_id = site_id
        self.custom_settings = {"DEPTH_LIMIT": max_depth}

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, "lxml")

        # Robust extraction, easily extensible
        extracted = {
            "title": soup.title.string.strip() if soup.title else "",
            "meta": {m.get("name") or m.get("property"): m.get("content") for m in soup.find_all("meta")},
            "h1": [h.get_text(strip=True) for h in soup.find_all("h1")],
            "h2": [h.get_text(strip=True) for h in soup.find_all("h2")],
            "main_text": "\n".join([p.get_text(strip=True) for p in soup.find_all("p")]),
            "images": [img.get("src") for img in soup.find_all("img") if img.get("src")],
            "css_files": [l.get("href") for l in soup.find_all("link", rel="stylesheet") if l.get("href")],
            "scripts": [s.get("src") for s in soup.find_all("script") if s.get("src")],
        }

        yield {
            "job_id": self.job_id,
            "site_id": self.site_id,
            "url": response.url,
            "status_code": response.status,
            "html_content": html,
            "extracted": extracted,
        }

        # Follow links (same domain)
        for link in soup.find_all("a", href=True):
            href = link["href"]
            yield response.follow(href, self.parse)
