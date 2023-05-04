from scrapy_redis.spiders import RedisSpider
import scrapy
from get_key import get_k
import logging

class GaoSpider(RedisSpider):
    name = "gao"
    start_urls = ["https://static-gkcx.gaokao.cn/www/2.0/json/live/v2/schoolnum.json"]
    logging.basicConfig(
        level=logging.ERROR,
        filename='app.log',
        filemode='w',
        format='%(name)s - %(levelname)s - %(message)s',
    )

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)

    def parse(self, response):
        data = dict(response.json()['data'])
        for domain in data.values():
            item = {
                'school_name': domain['school_name'],
                'province_id': domain['province_id'],
                'school_id': domain['school_id'],
            }
            print(item)
            for i in range(11, 66):
                url, data_json = get_k(i, item['school_id'])
                yield scrapy.Request(url=url, callback=self.parse_1)

    def parse_1(self, response):
        try:
            data = response.json()['data']
            print(data)
            for domain in data['item']:
                item_1 = {
                    'school_name': domain['name'],
                    'province_id': domain['city_name'],
                    'local_province_name': domain['local_province_name'],
                    'year': str(domain['year']),
                    'local_batch_name': domain['local_batch_name'],
                    'zslx_name': domain['zslx_name'],
                    'min_and_min_section': str(domain['min']) + '/' + str(domain['min_section']),
                    'proscore': 0 if domain['proscore'] == '-' else domain['proscore'],
                    'sg_info': domain['sg_info'],
                }
                yield item_1
        except Exception as e:
            logging.error('这里是错误信息\t' + str(e))
