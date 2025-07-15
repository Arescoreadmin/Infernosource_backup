# apps/backend/scraping/spiders/site_spider.py

import scrapy

class SiteSpider(scrapy.Spider):
    name = 'site_spider'

    def __init__(self, start_url=None, *args, **kwargs):
        super(SiteSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url] if start_url else []

    def parse(self, response):
        yield {
            'url': response.url,
            'html': response.text,
        }

        # Follow internal links
        for href in response.css('a::attr(href)').getall():
            yield response.follow(href, self.parse)
