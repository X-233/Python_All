# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import json
from random import choice
from time import sleep
from 学习.配置文件.随机请求头 import chrome
import parsel
import requests
from concurrent.futures import ThreadPoolExecutor


headers = {
    'user-agent': choice(chrome),
    'Referer': 'https://www.wchscu.cn/expertlist.html',
    }

headers1 = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Cookie': 'Secure; PHPSESSID=qan3j65hpea0kkkbip10qvc0qb; saw_terminal=default; Hm_lvt_84413645285d66c146b962a319e4628c=1679747807,1679752395; Secure; Hm_lpvt_84413645285d66c146b962a319e4628c=1679755587',
    'Host': 'www.wchscu.cn',
    'Referer': 'https://www.wchscu.cn/expertlist.html',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': choice(chrome),
    'X-Requested-With': 'XMLHttpRequest',
}

headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Secure; PHPSESSID=q4scqn85m7lr7il401pn60e9t8; saw_terminal=default; Hm_lvt_84413645285d66c146b962a319e4628c=1679756449; Secure; Hm_lpvt_84413645285d66c146b962a319e4628c=1679759047',
    'Host': 'www.wchscu.cn',
    'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': choice(chrome),
}

params = {
    'category_id': '820',
    'tpl_file': 'experts',
    'pagesize': 999,
    'title': '',
    'department': '',
}


def get_(func):
    def wrapper(*args):
        params['department'] = args[0]
        text_2 = func()
        return text_2

    return wrapper


@get_
def get_json():
    text_1 = requests.get(url=url, headers=headers1, params=params).text
    select1 = parsel.Selector(text_1)
    small_name = select1.xpath('//a/text()').getall()
    small_title = [url1 + m for m in select1.xpath('//a/@href').getall()]
    small = zip(small_name, small_title)
    return dict(small)


def dict_data():
    index = 0
    for i in all_1:

        big_title = i.xpath('.//span/text()').get()
        dict_list.append({"category": big_title, "departments": []})
        # dict_list[big_title] = {}

        for j in i.xpath('.//a'):
            data_id = j.xpath('./@data-id').get()
            middle_title = j.xpath('.//span/text()').get()
            dict_list[index]["departments"].append({"id": data_id, "department": middle_title, "professor": []})
            # dict_list[big_title].update({middle_title: data_id})
        index += 1
        print('#' * 30)


def get_1(func):
    def wrapper(*args, **kwargs):
        select_2 = func(*args, **kwargs)
        try:
            url_img = url1 + select_2.xpath('//div[@class="lbox"]/div[@class="img"]/img/@src').get()
            name_title = select_2.xpath('/html/head/meta[last()]/@content').get()
            if name_title:
                name_title = name_title.strip()
            tit = select_2.xpath('//div[@class="inner"]/div[@class="tit"]/text()').get()
            tit_1 = select_2.xpath('//div[@class="inner"]/div[@class="desc"]/text()').get()
            if tit_1:
                tit_1 = tit_1.strip().replace("专业特长：", "")
            return {'url_img': url_img, 'name_title': name_title, "professional": tit_1}
        except Exception as e:
            print(e)
            return {}

    return wrapper


@get_1
def get_html(url2):
    html = requests.get(url=url2, headers=headers2)
    print(html.status_code)
    select = parsel.Selector(html.text)
    return select


def get_html1():
    html = requests.get(url=url, headers=headers)
    select = parsel.Selector(html.text)
    return select


def save(key1, key_s1, small_11):
    # dict_list[key1][key_s1] = []
    dict_list.append({"category": key1, "departments": {"department": key_s1, "professor": []}})
    for key_1, value_1 in small_11.items():
        y = get_html(value_1)
        # print(key1,"+++++++++",key_s1,"+++++++++",key_1,"+++++++",y,"+++++++++")
        # dict_list[key1][key_s1].append({key_1: y})
        dict_list["departments"]["professor"].append(y)
        print("===============================================================\n")
        print(dict_list)
        print("===============================================================\n")


def wan(key_1, value_1):
    print(dict_list)


if __name__ == '__main__':
    url = 'https://www.wchscu.cn/expertlist.html'
    url1 = 'https://www.wchscu.cn'
    select_1 = get_html1()
    all_1 = select_1.xpath('//div[@class="tabsitem now"]/div')

    dict_list = []
    dict_data()

    url = 'https://www.wchscu.cn/searchs/expert.html'

    index = 0

    for i in dict_list:
        indexOf = dict_list.index(i)
        print(indexOf)
        for j in i["departments"]:
            small_1 = get_json(j["id"])
            for k, v in small_1.items():
                html = get_html(v)
                appendValue = {"name": k}
                appendValue.update(html)
                j["professor"].append(
                    appendValue
                )
                appendValue = {}

    # for keys, value_s in value_1.items():
    #     sleep(1)
    #     small_1 = get_json(value_s)
    #     save(key_1, keys, small_1)

    print('完成\t\n')
    with open('data_1.json', 'w', encoding='utf-8') as f:
        f.write(str(dict_list))
