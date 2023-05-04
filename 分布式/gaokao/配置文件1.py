"""
用来配置数据库
默认的数据条件
"""
import json
import pymysql
import requests
import redis

# 单例 + 上下文管理器
class Redis_fun_2:
    _instance = None  # 类属性用于记录实例对象

    def __new__(cls):
        if cls._instance is None:  # 如果还没有创建过程序的实例对象
            cls._instance = object.__new__(cls)  # 就创建一个新的实例对象
        return cls._instance  # 返回程序的实例对象

    def __init__(self):
        self.select_redis = redis_link[1]
        self.conn = redis.StrictRedis(
            host=self.select_redis['host'],
            port=self.select_redis['port'],
            password=self.select_redis['password'],
            db=1,
            decode_responses=True,
        )

    # 返回set类型数据列表
    def get_set_data(self, key_name):
        return [i.decode('utf-8') for i in self.conn.smembers(key_name)]

    # 返回list类型数据列表, 并且删除里面的值
    def get_list_data(self, key_name):
        data = []
        while True:
            data_1 = self.conn.lpop(key_name)
            if data_1:
                data.append(data_1)
            else:
                return data

    # 返回hash类型数据列表
    def get_hash_data(self, key_name):
        return self.conn.hvals(key_name)

    # 添加数据
    def push_list_data(self, key_name, values):
        self.conn.lpush(key_name, values)

    # 添加set集合
    def push_set_data(self, key_name, values):
        self.conn.sadd(key_name, values)

    # 添加hash数据
    def push_hash_data(self, key_name, values):
        self.conn.hmset(key_name, values)

    # 设置过期时间
    def set_ttl(self, key_name, time):
        self.conn.expire(key_name, time=time)

    def __enter__(self):
        print('开始连接数据库')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        print('关闭数据库连接')

class Mysql_fun:
    _instance = None  # 类属性用于记录实例对象

    def __new__(cls):
        if cls._instance is None:  # 如果还没有创建过程序的实例对象
            cls._instance = object.__new__(cls)  # 就创建一个新的实例对象
        return cls._instance  # 返回程序的实例对象

    def __init__(self):
        self.select_mysql = mysql_link[0]
        self.conn = pymysql.connect(
            user=self.select_mysql['user'],
            host=self.select_mysql['host'],
            port=self.select_mysql['port'],
            password=self.select_mysql['password'],
            database=self.select_mysql['database'],
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()
        self.sql = ''

    def search(self, cord):
        self.sql = 'select * from student where name = %s'
        self.cursor.execute(self.sql, (cord,))
        return self.cursor.fetchall()

    def __enter__(self):
        print('开始连接数据库')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        print('关闭数据库连接')


# 数据库连接配置
redis_link = [
    # 张辉
    {'password': 'zhanglin',
     'port': 6379,
     'host': '180.76.187.206',
     'redis_name': 'default'
     },
    # 代理池
    {'password': 'zhanglin',
     'port': 6379,
     'host': '47.115.203.82',
     'redis_name': 'default'
     },
]
mysql_link = [
    # 张辉
    {'user': 'zhanglin',
     'password': 'zhanglin',
     'host': '180.76.187.206',
     'port': 3306,
     'database': '毕设'
     },
    # # 毕设
    # {'mysql_name': 'root', 'mysql_key': 'zhanglin', 'mysql_ip': '175.155.64.40', 'mysql_port': 3306,
    #  'mysql_database': '毕设'},
]

# 随机请求头
chrome = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
          "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
          "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
          "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
          "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
          "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"]


def get_proxy():
    url = 'https://www.gaokao.cn/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    data = get_proxy_1()
    data_1 = []
    for i in data:
        print(i)
        # try:
        res = requests.get(url, proxies=i, headers=headers).status_code
        print(res)
        if res == 200:
            data_1.append(i)
        # except Exception as e:
        #     print(e)
        #     continue
    return data_1

def get_proxy_1():
    with Redis_fun_2()as redis_l:
        data = redis_l.get_hash_data('use_proxy')
    data_1 = []
    for i in data:
        data_1.append({'http': 'http://' + json.loads(i)['proxy']})
    print(data_1)
    return data_1
