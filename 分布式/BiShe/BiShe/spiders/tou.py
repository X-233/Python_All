import scrapy
from 头条解析 import tou_hot
from ..items import TouItem

class TouSpider(scrapy.Spider):
    name = 'tou'
    start_urls = ['https://www.toutiao.com/hot-event/hot-board/']

    def parse(self, response):
        Tou = TouItem()
        data = tou_hot(response.json())
        for i in data:
            Tou.update(i)
            yield Tou
