from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from 微博解析 import analysis, get_json
from ..items import WeiItem, Wei_contentItem
from urllib.parse import urlencode

class WeiContentSpider(RedisSpider):
    name = 'wei_content'
    redis_key = 'wei_hot_list'

    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        data = analysis(response.text)
        for i in data:
            item = WeiItem()
            item.update(i)
            data_dict = {
                'flow': '0',
                'is_reload': '1',
                'id': i['data_mid'],
                'is_show_bulletin': '2',
                'is_mix': '0',
                'max_id': 0,
                'count': '20',
                'uid': i['data_uid'],
                'fetch_level': '0',
            }
            url_1 = 'https://weibo.com/ajax/statuses/buildComments?' + urlencode(data_dict)
            yield Request(url=url_1, callback=self.parse_1, meta={'data_mid': i['data_mid'], 'data_uid': i['data_uid']}, dont_filter=True)
            yield item

    def parse_1(self, response):
        data = response.json()['data']
        data_mid = response.meta['data_mid']
        data_uid = response.meta['data_uid']
        data_1 = get_json(data)
        max_id = response.json()['max_id']
        print(response.url)
        for i in data_1:
            item_1 = Wei_contentItem()
            item_1.update(i)
            yield item_1
        data_dict = {
            'flow': '0',
            'is_reload': '1',
            'id': data_mid,
            'is_show_bulletin': '2',
            'is_mix': '0',
            'max_id': max_id,
            'count': '20',
            'uid': data_uid,
            'fetch_level': '0',
        }
        url_1 = 'https://weibo.com/ajax/statuses/buildComments?' + urlencode(data_dict)
        yield Request(url=url_1, callback=self.parse_1, meta={'data_mid': data_mid, 'data_uid': data_uid})
