# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import parsel
import requests


def header():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    return headers


if __name__ == '__main__':
    url = 'https://www.89ip.cn/'
    html = requests.get(url=url, headers=header())
    select = parsel.Selector(html.text)
    x = select.xpath('//tbody/tr')
    data = []
    for i in x:
        ip = i.xpath('./td[1]/text()').get().strip()
        port = i.xpath('./td[2]/text()').get().strip()
        data.append({'http': 'http://' + str(ip) + ':' + str(port)})
    with open('proxies.txt', 'w', encoding='utf-8') as f:
        f.write(str(data))
    # with open(r'D:\IDEA\Project\学习\分布式\gaokao\proxies.txt', 'w', encoding='utf-8') as f:
    #     f.write(str(data))
