# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import hmac
from urllib.parse import urlencode
import hashlib
import base64
params = {
    'e_sort': 'zslx_rank,min',
    'e_sorttype': 'desc,desc',
    'local_province_id': '15',
    'page': '1',
    'school_id': '140',
    'size': '10',
    'uri': 'apidata/api/gk/score/province',
    'year': '2022',
}


def get_k(local_province_id, school_id):
    params['local_province_id'] = str(local_province_id)
    params['school_id'] = str(school_id)
    key = b'D23ABC@#56'
    url_2 = urlencode(params)
    url_1 = b'api.eol.cn/web/api/?' + bytes(url_2, encoding='utf8')

    # print(url_1)
    result = hmac.new(key=key, msg=url_1, digestmod=hashlib.sha1).digest()
    _result = base64.b64encode(result).decode()
    # print(_result)

    result = hmac.new(key=key, msg=result, digestmod=hashlib.md5).hexdigest()
    # print(result)

    params.update({'signsafe': result})
    url_2 = urlencode(params)
    url_2 = 'https://api.eol.cn/web/api/?' + url_2
    return url_2, params
