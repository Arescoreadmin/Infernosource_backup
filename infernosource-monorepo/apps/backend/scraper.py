from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apps.backend.scraping.spiders.competitor_spider import CompetitorSpider

def scrape_site(start_url):
    process = CrawlerProcess(get_project_settings())
    results = []

    def collect_result(item, response, spider):
        results.append(item)

    CompetitorSpider.parse = staticmethod(CompetitorSpider.parse)
    crawler = process.create_crawler(CompetitorSpider)
    crawler.signals.connect(collect_result, signal=crawler.signals.item_scraped)
    process.crawl(crawler, start_url=start_url)
    process.start()

    return results
