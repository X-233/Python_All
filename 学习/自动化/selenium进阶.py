import requests
import json
import parsel
from selenium.webdriver import Chrome, ChromeOptions, ActionChains


class Request:
    def __init__(self):
        self.url = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        self.data = ''
        self.params = ''
        self.ip = ''
        self.json = ''
        self.urls = ''

    @staticmethod
    def dct(func):
        def wrapper(*args, **kwargs):
            resp, tag = func(*args, **kwargs)
            if tag == 'get_text':
                print('是get_text类型')
            if tag == 'get_content':
                print('是get_content类型')
            if tag == 'get_json':
                print('是get_json类型')
            if tag == 'post_json':
                print('是post_json类型')

        return wrapper

    @dct
    def get_text(self):
        resp = requests.get(self.url, headers=self.headers).text
        select = parsel.Selector(resp)
        return select, 'get_text'

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

class Chrome1:

    def __init__(self):
        self.url = ''
        self.web = webdriver.Chrome()

if __name__ == '__main__':
    data = Request()
    data.url = 'https://cn.bing.com/'

    web_1 = Chrome1()
    web_1
