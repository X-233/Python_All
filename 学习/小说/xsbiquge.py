from time import sleep
import requests
import json
import parsel
from random import choice

class Request:

    def __init__(self):
        self.url = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        self.data = ''
        self.params = ''
        self.ip = []
        self.json = ''
        self.urls = ''
        self.cookie = ''

    @staticmethod
    def dct(func):
        def wrapper(*args, **kwargs):
            resp, tag = func(*args, **kwargs)
            if tag == 'get_text':
                return resp
        return wrapper

    @dct
    def get_text(self):
        while True:
            try:
                resp = requests.get(self.url, headers=self.headers).text
                select = parsel.Selector(resp)
                return select, 'get_text'
            except Exception as e:
                sleep(20)
                print(e)

    @dct
    def get_content(self):
        resp = requests.get(self.url, headers=self.headers).content
        return resp, 'get_content'

    @dct
    def get_json(self):
        resp = requests.get(self.url, headers=self.headers, params=self.params).json()
        return resp, 'get_json'

    @dct
    def post_json(self):
        resp = requests.post(self.url, headers=self.headers, data=self.data, json=self.json).json()
        return resp, 'post_json'

    def get_ip(self):
        with open('D:\IDEA\Project\学习\学习\配置文件\proxies.txt', 'r') as file:
            self.ip = eval(file.read())


if __name__ == '__main__':
    data = Request()
    data.get_ip()
    data.url = 'http://www.xsbiquge.org/book/' + '3410'
    resp_1 = data.get_text()
    resp_2 = resp_1.xpath('//div[@class="container border3-2 mt8 mb20"]/div[@class="info-chapters flex flex-wrap"]')
    resp_3 = ['http://www.xsbiquge.org' + j for j in resp_2.xpath('./a/@href').getall()]
    data.urls = resp_3
    for i in data.urls:
        data.url = i
        resp_4 = data.get_text()
        title = resp_4.xpath('//h1/text()').get().split('（')[0] + '\n'
        if_next = resp_4.xpath('//a[@id="next_url"]/text()').get()
        next_url = resp_4.xpath('//a[@id="next_url"]/@href').get()
        article = ''.join(resp_4.xpath('//article[@id="article"]/p/text()').getall()).replace('\r\r', '\n')
        if '下一页' in if_next:
            data.url = 'http://www.xsbiquge.org' + next_url
            resp_4 = data.get_text()
            article2 = ''.join(resp_4.xpath('//article[@id="article"]/p/text()').getall()).replace('\r\r', '\n')
            article += article2
        with open('这游戏也太真实了.txt', 'a', encoding='utf-8') as f:
            f.write(title + article + '\n\n')
        print(title + '保存成功\n')
