from scrapy import Request
from 数据库方法 import get_tou_hot
from 头条解析 import tou_content
from ..items import TouContentItem
from scrapy_redis.spiders import RedisSpider

class TouHotSpider(RedisSpider):
    name = 'tou_hot'
    # start_urls = get_tou_hot('tou_list')
    redis_key = 'tou_hot_list'
    # redis_batch_key = 'myspider:batch'

    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        data = response.json()
        if (response.meta['sum_1']) < data['total_number']:
            yield Request(response.url, callback=self.parse, meta={'sum_1': data['offset']})
        data_1 = tou_content(data)
        for i in data_1:
            item = TouContentItem()
            item['user_name'] = i['user_name']
            item['user_id'] = i['user_id']
            item['text'] = i['text']
            item['open_url'] = i['open_url']
            item['source_id'] = response.url.split('item_id=')[-1]
            yield item

