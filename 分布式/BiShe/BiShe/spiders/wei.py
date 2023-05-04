import scrapy
from 微博解析 import analysis_topic

class WeiSpider(scrapy.Spider):
    name = "wei"
    start_urls = ["https://weibo.com/ajax/side/hotSearch"]

    def parse(self, response):
        data = response.json()['data']['realtime']
        data_1 = analysis_topic(data)
        for i in data_1:
            yield i
