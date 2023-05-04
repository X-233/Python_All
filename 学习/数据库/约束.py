# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
from 学习.配置文件.数据库 import link_sql

class sql:
    def __init__(self):
        self.conn = link_sql(1)
        self.cursor = self.conn.cursor()

    def findall(self, age):
        self.cursor.execute(f'SELECT * FROM bads WHERE age > 18 and age < 24')
        return self.cursor.fetchall()

    def __enter__(self):
        print('进入上下文管理器!')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        print('退出上下文管理器!')
