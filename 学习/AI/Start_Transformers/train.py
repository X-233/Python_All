import re

with open('这游戏也太真实了.txt', 'r', encoding='utf-8')as f:
    text = f.readlines()

step = 0
data = []
for line in text:
    try:
        if line + text[text.index(line) + 1] == '.\n\n':
            role = 'title:\t' + text[text.index(line) + 2].strip()
        else:
            line = line.strip()
            if line[0] == '“' and line[-1] == '”':
                role = 'role:\t' + line
            elif line[0] != '“' and line[-1] == '”':
                other = line.split('：')
                role = f'{other[0]}:\t' + other[-1]
            else:
                role = 'narrator:\t' + line
        data.append(role)
    except Exception as e:
        role = ''
    step += 1
    if step % 1000 == 0:
        data_1 = '\n'.join(data)
        with open('data_xs.txt', 'a', encoding='utf-8') as f:
            f.write(data_1 + '\n')
        data = []
        print(line)
else:
    data_1 = '\n'.join(data)
    with open('data_xs.txt', 'a', encoding='utf-8') as f:
        f.write(data_1 + '\n')

'题目：分布式爬虫与数据融合系统，环境: pycharm, python, ubuntu22.04, mysql, redis, nodejs,  python第三方库: parsel, requests, scrapy_redis, scrapy, execjs, csv, pymysql, redis'
