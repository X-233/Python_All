import requests

class Get:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    params = {
        'mode': '13',
        'dm': '4',
        'cwidth': '1596',
        'cheight': '1064',
        'start': 0,
        'xml_len': 50,
        'query': '壁纸',
    }
    url = 'https://pic.sogou.com/napi/pc/searchList'

    @staticmethod
    def get_(func):
        def wrapper(*args, **kwargs):
            index = args[1]
            while index:
                json_data = func(*args, **kwargs)
                Get.params['start'] = Get.params['xml_len'] * index
                yield json_data
                index -= 1
        return wrapper

    @get_
    def get_json(self, num_1):
        res = requests.get(self.url, headers=self.headers, params=self.params)
        if res.status_code == 200:
            print('请求成功！')
        return res.json()

if __name__ == '__main__':
    get_d = Get()
    for i in get_d.get_json(5):
        print(i['info'])
