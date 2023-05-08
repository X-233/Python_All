import json
import re
from concurrent.futures import ThreadPoolExecutor
from time import time

import requests
import parsel

from 学习.配置文件.数据库 import Mysql_fun


class Request:
    def __init__(self):
        self.url = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'Cookie': '_octo=GH1.1.1826208031.1681195859; _device_id=8eac216620a2c5f956a80604421bb63e; user_session=DucEqWwJDiFfQUtqLzpv7vv1U9zudJS3LCeh2NUsItAWWcEf; __Host-user_session_same_site=DucEqWwJDiFfQUtqLzpv7vv1U9zudJS3LCeh2NUsItAWWcEf; logged_in=yes; dotcom_user=X-233; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light_high_contrast%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=S6yfX5A9rkWi0WOFD7i9VmDvi0V3mS2wLmJrv%2Bvsn69HkVgPcpTGsHmGyHPOD6o2Bz4b5sYz3eCVC5eZerywaBjjDKgm0By9aaFsvLvgIFDHlBb0%2BPjXqeMMzAamzQ4xSYKDr4dhIcfkYh8ox0hEUBZQ5VK6YhEM4lk%2F1iXrXIOoQKEzwjNSMuz239I8qGe58FMDy945U0WN1V9ZHZixHV8UQP4L4mUYIQuD8kcSYIMmZOdRpqx5Yn0df0laBC1qDtHZcQ63lPjQfMB19TSDfNGh02zIZKnGNC5%2F1gt4azBmZRXxGSVag4%2FcZ9IvABLT%2F0a55sO8t73BLy8TRg%3D%3D--FjbDzC8DXeK7TOQ6--rxoUaAVlyRnFI5ss50dbbw%3D%3D'
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
                return resp
            if tag == 'get_content':
                print('是get_content类型')
            if tag == 'get_json':
                print('是get_json类型')
            if tag == 'post_json':
                print('是post_json类型')

        return wrapper

    @dct
    def get_text(self):
        resp = requests.get(self.url, headers=self.headers)
        print(resp.status_code)
        resp = requests.get(self.url, headers=self.headers).text
        # with open('htmll.html', 'w', encoding='utf-8') as file:
        #     file.write(resp)
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

def run(url_1):
    data_1 = Request()
    data_1.url = url_1
    select_1 = data_1.get_text()

    tds = select_1.xpath('//tbody/tr')
    for td in tds:
        text_1 = td.xpath('./td/text()').getall()
        data_2 = {
            'title': text_1[0],
            'hot': text_1[1],
        }
        data1.append(data_2)
        print(data_2)

if __name__ == '__main__':
    # data = Request()
    # data.url = 'https://github.com/PlexPt/chatgpt-corpus/blob/main/question/README.md'
    # select1 = data.get_text()
    #
    # text = select1.xpath('//td/a/text()').getall()
    # text_url = ['https://github.com' + re.findall('"(.*?)\\\\', i)[0] for i in select1.xpath('//td/a/@href').getall()]
    # data1 = []
    #
    # start_time = time()
    # # run(text_url[0])
    # with ThreadPoolExecutor(max_workers=10)as pool:
    #     for i in text_url:
    #         pool.submit(run, i)
    #         print(i)
    # print('总共用时:\t' + str(time() - start_time))

    # with open('69万问题.txt', 'r', encoding='utf-8') as f:
    #     data1 = eval(f.read())
    # with open('69万问题2.txt', 'w', encoding='utf-8') as f:
    #     for line in data1:
    #         f.write(str(line) + '\n')

    data2 = []
    data3 = 0
    with open('69万问题2.txt', 'r', encoding='utf-8') as f:
        data1 = f.readlines()
    for line in data1:
        data3 += 1
        da = eval(line)
        if data3 % 10000 == 0:
            with Mysql_fun(1) as link:
                link.sql = "insert into 69万问题 values(%s, %s, %s);"
                link.cursor.executemany(link.sql, data2)
            data2 = []
        data2.append((0, da['title'], da['hot']))
    else:
        with Mysql_fun(1) as link:
            link.sql = "insert into 69万问题 values(%s, %s, %s);"
            link.cursor.executemany(link.sql, data2)

