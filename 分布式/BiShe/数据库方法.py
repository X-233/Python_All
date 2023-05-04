import pymysql
import redis
from 配置文件 import redis_link, mysql_link
import json

# 单例 + 上下文管理器
class Redis_fun:
    _instance = None  # 类属性用于记录实例对象

    def __new__(cls):
        if cls._instance is None:  # 如果还没有创建过程序的实例对象
            cls._instance = object.__new__(cls)  # 就创建一个新的实例对象
        return cls._instance  # 返回程序的实例对象

    def __init__(self):
        self.select_redis = redis_link[0]
        self.conn = redis.StrictRedis(
            host=self.select_redis['host'],
            port=self.select_redis['port'],
            password=self.select_redis['password'],
            db=0,
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


# with Mysql_fun()as mysql_1:


# 获取头条hot
def get_tou_hot(name):
    """
    :param name: key name, 例如: tou_list
    :return: list
    """
    list_1 = []
    with Redis_fun()as redis_link_1:
        for i in redis_link_1.get_list_data(name):
            list_1.append(json.loads(i)['Url'])
    return list_1

# if __name__ == '__main__':
#     with Redis_fun()as redis_1:
#         redis_1.push_list_data('ceshi', '123')
#         redis_1.push_list_data('ceshi', '123')
#         redis_1.push_list_data('ceshi', '123')
#         # redis_1.set_ttl('ceshi', 20)
#
#         list_2 = redis_1.get_list_data('ceshi')
#         print(list_2)
#     with Redis_fun()as redis_2:
#         redis_2.push_list_data('ceshi', '123')
#         redis_2.push_list_data('ceshi', '123')
#         redis_2.push_list_data('ceshi', '123')
#         # redis_1.set_ttl('ceshi', 20)
#
#         list_2 = redis_2.get_list_data('ceshi')
#         print(list_2)
#     print(id(redis_1))
#     print(id(redis_2))

