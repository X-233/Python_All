from scrapy import signals
from 配置文件 import get_cookie_dict, chrome, get_sign
from urllib.parse import urlencode
import requests


class BisheDownloaderMiddleware:
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
        if spider.name == 'wei_content':
            request.cookies = get_cookie_dict('微博')
            request.headers['User-Agent'] = chrome

        if spider.name == 'wei':
            request.cookies = get_cookie_dict('微博')
            request.headers['User-Agent'] = chrome

        if spider.name == 'tou':
            request.headers['User-Agent'] = chrome
            request.referer = 'https://www.toutiao.com/'
            request.cookies = get_cookie_dict('头条')
            # request.meta['proxy'] = '127.0.0.1:7890'
            signs = get_sign()
            params = {
                'origin': 'toutiao_pc',
                '_signature': signs
            }
            request._set_url(request.url + '?' + urlencode(params))
            print(request.url)

        if spider.name == 'tou_hot':
            url = 'https://www.toutiao.com/article/v2/tab_comments/'
            request.headers['User-Agent'] = chrome
            # request.referer = request.url
            request.cookies = get_cookie_dict('头条')
            try:
                i_1 = request.meta['sum_1']
            except KeyError:
                i_1 = 0
                request.meta['sum_1'] = 0
            signs = get_sign()
            topic_id = request.url.split('item_id=')[-1]
            params = {
                'aid': '24',
                'app_name': 'toutiao_web',
                'offset': i_1,
                'count': 40,
                'group_id': topic_id,
                '_signature': signs,
                'item_id': topic_id,
            }
            request._set_url(url + '?' + urlencode(params))

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

