import redis
import pymysql

# 数据库连接配置
redis_link = [
    # 张辉
    {'password': 'zhanglin',
     'port': 6379,
     'host': '180.76.187.206',
     'redis_name': 'default'
     },
    # # 代理池
    {'redis_key': 'zhanglin',
     'redis_port': 6379,
     'ip': '47.115.203.82',
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
    {'user': '阿里云',
     'password': 'zhanglin',
     'host': '47.115.203.82',
     'port': 3306,
     'database': '阿里云'
     },
]

class Mysql_fun:
    _instance = None  # 类属性用于记录实例对象

    def __new__(cls, d):
        if cls._instance is None:  # 如果还没有创建过程序的实例对象
            cls._instance = object.__new__(cls)  # 就创建一个新的实例对象
        return cls._instance  # 返回程序的实例对象

    def __init__(self, d):
        """
        :param d:0是百度云, 1是阿里云
        """
        self.select_mysql = mysql_link[d]
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
