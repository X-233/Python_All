import requests
import json
import parsel
from selenium.webdriver import ChromeOptions, ActionChains, Chrome
from selenium.webdriver.common.by import By


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


if __name__ == '__main__':
    data = Request()
    data.url = 'https://cn.bing.com/'

    # 添加参数
    options = ChromeOptions()

    # 创建对象
    web = Chrome(options=options)
    web.get('https://fgnwct.com/login.html')
    web.maximize_window()
    #显式等待
    web.implicitly_wait(10)

    # 找到元素
    web.find_element(By.CSS_SELECTOR, '#email').send_keys('1972125164@qq.com')
    web.find_element(By.CSS_SELECTOR, '#password').send_keys('zhanglin')
    web.find_element(By.CSS_SELECTOR, '.form-control.btn.btn-primary').click()

    input()

