# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰

from concurrent.futures import ThreadPoolExecutor
import requests
import re
from random import choice
import json
import os
import subprocess
from lxml import etree
import redis

word = input('请输入要下载视频的网址:\n')

H = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
     'Referer': word,
     'cookie': "buvid3=6FD54052-2816-9513-C9F0-DBD0101562E095064infoc; b_nut=1681138095; i-wanna-go-back=-1; _uuid=B9CFDCFB-3CD7-3751-75D4-C65DA4B8DC4A99376infoc; home_feed_column=5; nostalgia_conf=-1; CURRENT_FNVAL=4048; CURRENT_PID=f04f65d0-d7ae-11ed-9727-fd7c99c0ac09; rpdid=|(J|YJJulJmR0J'uY)uuJ)u)l; header_theme_version=CLOSE; DedeUserID=514671750; DedeUserID__ckMd5=9b4aa2e41166602b; fingerprint=fb72d5a8df91f9340ec07a0409922d5f; buvid_fp_plain=undefined; PVID=1; b_ut=5; FEED_LIVE_VERSION=V8; buvid_fp=fb72d5a8df91f9340ec07a0409922d5f; SESSDATA=9dc66bad%2C1697029397%2C68111%2A42; bili_jct=9ea82f12c1be65989be93c3e39578d05; sid=6hc87d3i; b_lsid=5E107EA9D_18783E08F27; bp_video_offset_514671750=784707460240769000; buvid4=A2856B49-9ECD-12ED-17FC-A7505FCBB16297072-023041022-TNlJn+y0Jb0TgG7rSqJNrw%3D%3D; innersign=1; CURRENT_QUALITY=80"
     },
]

if not os.path.exists('video'):
    os.mkdir('video')


def Analysis_start():
    url = word
    text_s = requests.get(url=url, headers=choice(H))

    text_s = text_s.text
    # str_1 = (re.findall('<span class="cur-page">(.*?)</span>', text_s, re.S))[0]
    html = etree.HTML(text_s)
    title = html.xpath('//*[@id="viewbox_report"]/h1/@title')[0]

    str_2 = (re.findall('<script>window.__INITIAL_STATE__=(.*?)</script>', text_s, re.S))[0]
    str_3 = re.findall('(.*?);\\(function\\(\\)', str_2)[0]
    # print(str_3)

    json_2 = json.loads(str_3)
    # pprint.pprint(json_2)
    #
    # with open('1.json', 'w', encoding='utf-8')as f:
    #     f.write(str(json_2))

    item = {}
    Inf = json_2['videoData']['pages']
    for i in Inf:
        part = re.sub('[\d+]', '', i['part'])
        part = re.sub(' ', '', part)
        #strip是把空格删除,方便后面文件读写
        item[str(i['page']) + '_' + (str(part).strip())] = word + '?p=' + str(i['page'])
    print(item)

    return item, str(title).replace(' ', '_')

def Analysis(text_1, url, text_3):
    text = requests.get(url=url, headers=choice(H), timeout=10)
    # f = open('1.html', 'w', encoding='utf-8')
    # f.write(text.text)
    # f.close()
    # text_1 = (re.findall('class="video-title tit">(.*?)</h1>', text.text, re.S))[0]
    #找到包含视频网址的数据
    text_2 = re.findall('<script>window.__playinfo__=(.*?)</script>', text.text, re.S)
    # print(text_1[0])
    # print(json.loads(text_2[0]))
    json_1 = json.loads(text_2[0])

    # pprint.pprint(json_1)
    str_1 = json_1['data']['dash']['audio'][0]['baseUrl']
    str_2 = json_1['data']['dash']['video'][0]['baseUrl']
    # print(str_1)
    # print(str_2)
    print('正在下载......')
    re_1 = requests.get(url=str_1, headers=choice(H)).content
    re_2 = requests.get(url=str_2, headers=choice(H)).content

    if not os.path.exists(f'D:\\视频\\爬虫\\{text_3}'):
        os.mkdir(f'D:\\视频\\爬虫\\{text_3}')

    with open('video\\' + text_1 + '.mp3', mode='wb')as f_1:
        f_1.write(re_1)
    with open('video\\' + text_1 + '.mp4', mode='wb')as f_2:
        f_2.write(re_2)

    print('下载完成\t' + text_1)

    print('正在合成')
    if os.path.exists(f'video\\{text_1}.mp4'):
        # 'https://www.bilibili.com/video/BV1t94y1f7Ex'
        # 'https://www.bilibili.com/video/BV15F411s7Qd'
        COMMAND = f'D:\\FFmpeg\\bin\\ffmpeg.exe -i video\\{text_1}.mp3 -i video\\{text_1}.mp4 -codec copy D:\\视频\\爬虫\\{text_3}\\{text_1}.mp4'
        # COMMAND = f'D:\\FFmpeg\\bin\\ffmpeg.exe -i video\\{text_1}.mp3 -i video\\{text_1}.mp4 -c:v copy -c:a acc -strict experimental video_1\\{text_1}output.mp4'
        subprocess.run(COMMAND, shell=True, encoding='gbk', stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        # , stdout = subprocess.PIPE, stderr = subprocess.STDOUT


if __name__ == '__main__':
    pool = ThreadPoolExecutor(3)
    list_url, title = Analysis_start()
    for key, value in list_url.items():
        if not os.path.exists(f'D:\\视频\\爬虫\\{title}\\{key}.mp4'):
            pool.submit(Analysis, key, value, title)
            # print(key)
    pool.shutdown(wait=True)
    if os.path.exists('video'):
        COMMAND2 = f'rd /s/q video'
        subprocess.run(COMMAND2, shell=True, encoding='utf-8')
