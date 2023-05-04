# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import parsel
import requests
from 学习.配置文件.随机请求头 import chrome
from random import choice

def header():
    headers = {
        'user-agent': choice(chrome),
        'cookie': 'SINAGLOBAL=3498801263665.5874.1680845828403; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWRgbmjOYp6la8.q2UBvMq_5JpX5KMhUgL.FoM7S0qEShMce0.2dJLoI0qLxK.LB.2LBKqLxK-LB.BL1KeLxKBLBonLB-2LxKnL1K5L1-BLxK-L12BL1-eLxKnL1h5LBoqt; ALF=1683441138; SSOLoginState=1680849139; SCF=ApB1X555ntiVvQB0Yv7gn7_W7die9XJnemRkL_sXhyx69bzvxlinMHMzDjJBvUMT0Gwm__xc0NjhmxjhtW3up18.; SUB=_2A25JK8ikDeRhGeFO7FQT9CnKyDWIHXVqQL1srDV8PUNbmtANLXOikW9NQVsPXhmdEG3z4UWelMhqGu-0Ic-n71tT; _s_tentry=weibo.com; Apache=7407959195627.196.1680849146830; ULV=1680849146862:2:2:2:7407959195627.196.1680849146830:1680845828419'
    }
    return headers

data_1 = {
    "path": '/IOS更多资源',
    "password": "",
    "page": 1,
    "per_page": 100,
    "refresh": False
}

if __name__ == '__main__':
    url = 'https://s.weibo.com/weibo?q=%23%E7%A5%9E%E5%8D%81%E4%BA%94%E8%88%AA%E5%A4%A9%E5%91%98%E5%9C%A8%E8%BD%A8%E5%B7%A5%E4%BD%9C%E6%9C%89%E5%A4%9A%E5%BF%99%23&topic_ad='
    html = requests.get(url=url, headers=header())
    print(html.status_code)
    print(html.text)
