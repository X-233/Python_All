import scrapy


class ChinadaSpider(scrapy.Spider):
    name = "chinada"
    allowed_domains = ["chinadaily.com"]
    start_urls = ["http://chinadaily.com/"]

    def parse(self, response):
        pass
