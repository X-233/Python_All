import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import requests
import json
import parsel
from 学习.配置文件.数据库 import Mysql_fun


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
                # print('是get_text类型')
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
        # sleep(0.3)
        resp = requests.get(self.url, headers=self.headers)
        # print(resp.status_code)
        resp = resp.text
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

def parsing(y):
    data.url = f'https://yinghuadongman.me/tv-0-{y}-%E6%97%A5%E6%9C%AC-rating-0-30.html'
    while True:
        select_1 = data.get_text()
        select_2 = select_1.css('.b007>div')
        if select_2:
            next_page = 'https://yinghuadongman.me' + select_1.xpath('//div[@id="page"]//li[last()]/a/@href').get()
            data.url = next_page
            data_1 = parsing2(select_2)
            print(f'\n爬取的是第\t{y}\t年的')
            for k in data_1:
                print(k)
                yield k
        else:
            break
        print(len(select_2))

def parsing2(sel):
    for k1 in sel:
        url = 'https://yinghuadongman.me' + k1.css('a::attr(href)').get()
        name = k1.css('a>span::text').get()
        score = k1.css('a>span>em::text').get()
        img = k1.css('img::attr(src)').get()
        time_1 = k1.css('a>div>span::text').get()
        seed = parsing_3(url)
        data_dict = {
            'url': url,
            'name': name,
            'score': score,
            'img': img,
            'time_1': time_1,
            'seed': seed
        }
        sleep(0.5)
        yield data_dict

def parsing_3(url):
    data_8 = []
    data1.url = url
    select_3 = data1.get_text()
    seed1 = select_3.css('li>div')
    for k2 in seed1:
        xx = k2.css('.copylink::attr(alt)').get()
        xy = k2.css('a::text').get()
        data_8.append(xy + '|-->|' + xx)
    seed2 = ', '.join(data_8)
    return seed2

def run(y2):
    for j in parsing(y2):
        data_all.append(j)

if __name__ == '__main__':
    data = Request()
    data1 = Request()

    years = [str(i) for i in range(2010, 2023)]
    years.append('更早')

    data_all = []
    pool = ThreadPoolExecutor(max_workers=10)
    for y1 in years:
        pool.submit(run, y1)

    pool.shutdown(wait=True)

    with open('动漫url.json', 'w', encoding='utf-8')as f:
        f.write(json.dumps(data_all))

    with open('动漫url.json', 'r')as f:
        data_4 = json.loads(f.read())

    print(data_4)
    data_5 = []
    for i in data_4:
        score = i['score']
        if i['score'] == '- -':
            score = 0.0
        data_6 = (0, i['url'], i['name'], score, i['img'], i['time_1'], i['seed'])
        data_5.append(data_6)

    with Mysql_fun(1)as link:
        link.sql = "insert into 动漫 values(%s, %s, %s, %s, %s, %s, %s);"
        link.cursor.executemany(link.sql, data_5)


