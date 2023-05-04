# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
from random import choice
from time import sleep
import parsel
import requests
from 学习.配置文件.随机请求头 import chrome


headers = {'user-agent': choice(chrome)}


data_1 = {
    "path": '',
    "password": "",
    "page": 1,
    "per_page": 100,
    "refresh": False
}

data_2 = {}
data_3 = ['']

# 装饰器
def bool_html(func):
    # 暂存func
    def wrapper(*args, **kwargs):
        try:
            select, html = func(*args, **kwargs)
            if str(html.status_code)[0] == '2':
                print('网址请求成功: \t' + args[0])
                # 返回选择器
                return select
            else:
                print('网址请求失败: \t' + args[0])
        except Exception as e:
            print(e)
    # 返回func
    return wrapper

@bool_html
def request_get(url1):
    sleep(4)
    html = requests.get(url=url1, headers=headers)
    html.encoding = html.apparent_encoding
    select = parsel.Selector(html.text)
    return select, html

@bool_html
def request_post(url2):
    sleep(4)
    html = requests.post(url=url2, headers=headers, data=data_1)
    json_ = html.json()
    # print(json_)
    return json_, html

def yield_1(json2):
    while True:
        sleep(3)
        len_1 = [i_1['data']['content'] for i_1 in json2]
        for i_1 in len_1:
            for j in i_1:
                # 在这里拼接文件路径，data_3的len对应选择器的len，就是json2的
                data_2.update({j['name']: data_3[len_1.index(i_1)] + '/' + j['name']})

        json2 = []
        data_3.clear()

        for i_1 in len_1:
            for j in i_1:
                # 判断是否是目录
                if j['is_dir']:
                    # 技巧
                    # print(data_2[j['name']])
                    # 用名字去判断是否属于该目录
                    data_1['path'] = data_2[j['name']]
                    # 填入目录名称
                    data_3.append(data_2[j['name']])

                    # json2的len就是data_3的len，对应
                    json2.append(request_post(url_2))

                    data_1['path'] = ''
                else:
                    j.update({'path_1': data_2[j['name']]})
                    print(j['name'])
                    yield j

if __name__ == '__main__':
    url_1 = 'https://cdbzy.com/'
    url_2 = 'https://cdbzyz.com/api/fs/list/'
    select_1 = request_get(url_1)
    json_2 = [request_post(url_2)]

    # 打印， 基本信息
    title = select_1.xpath('//title/text()').get()
    # print(title + '\n')

    y_1 = yield_1(json_2)

    list_all = []
    for i in y_1:
        with open('苹果软件列表_1.txt', 'a', encoding='utf-8')as f:
            f.write(str(i) + '\n')
        print(i)
