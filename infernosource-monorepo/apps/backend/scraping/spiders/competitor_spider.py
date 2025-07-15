import scrapy

class CompetitorSpider(scrapy.Spider):
    name = "competitor_spider"

    def __init__(self, start_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [start_url]

    def parse(self, response):
        yield {
            "url": response.url,
            "html": response.text,
        }

        for href in response.css('a::attr(href)').getall():
            yield response.follow(href, callback=self.parse)
