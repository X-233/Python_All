# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import json
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
#键盘操作
from selenium.webdriver.common.keys import Keys
from time import sleep
#下拉select,css动态加载出来的
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import parsel
import requests
from 学习.配置文件.随机请求头 import chrome
from random import choice

class Get_data:
    headers = {
        'user-agent': choice(chrome),
        }

    params = {
    }

    url = ''

    data = ''

    @staticmethod
    def get(func):
        def wrapper(*args):
            html_1 = func(*args)
            select = parsel.Selector(html_1.text)
            return select
        return wrapper

    @staticmethod
    @get
    def post_html(url1):
        html1 = requests.post(url=url1, headers=Get_data.headers, data=Get_data.params)
        return html1

    @staticmethod
    @get
    def get_html(url2):
        html1 = requests.get(url=url2, headers=Get_data.headers)
        return html1

    @staticmethod
    def get_html_1(url3):
        html1 = requests.get(url=url3, headers=Get_data.headers_1, params=Get_data.params)
        return html1

    @staticmethod
    def start():
        # 存储数据
        with open('data_1.text', 'w', encoding='utf-8') as f:
            f.write(str(Get_data.data))

    @staticmethod
    def selenium_1(url4):
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        web = Chrome(options=options)
        web.maximize_window()
        web.get(url=url4)

if __name__ == '__main__':
    get_dat = Get_data()
    get_dat.url = ''

