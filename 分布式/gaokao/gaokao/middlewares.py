# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from random import choice
from 配置文件1 import chrome
import requests

class GaokaoDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.headers['User-Agent'] = choice(chrome)
        # ip = 'http://' + requests.get('http://47.115.203.82:5010/get/').json()['proxy']
        # request.meta['proxy'] = ip

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception, Exception):
            # print(request.meta['proxy'])
            return request

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
