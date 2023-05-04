from 数据库方法 import Mysql_fun, Redis_fun
import json

# 一次性取多少
def batch_pop(key, n):
    with Redis_fun() as redis_1:
        p = redis_1.conn.pipeline()
        p.lrange(key, 0, n - 1)
        p.ltrim(key, n, -1)
        data = p.execute()[0]
    data2 = []
    for i in data:
        data1 = []
        for j in json.loads(i).values():
            data1.append(j)
        data1 = [0] + data1
        data2.append(tuple(data1))
    return data2

def insert_sql(name, data):
    with Mysql_fun()as mysql_1:
        try:
            placeholders = ', '.join(['%s'] * len(data[0]))  # 生成占位符
        except Exception as e:
            print(e)
            return None
        mysql_1.sql = f'insert into {name} values({placeholders});'
        mysql_1.cursor.executemany(mysql_1.sql, data)

def insert_update_tou(name, data):
    with Mysql_fun()as mysql_1:
        for k in data:
            placeholders = ', '.join(['%s'] * len(k))  # 生成占位符
            mysql_1.sql = f"insert into {name} values({placeholders}) on duplicate key update source_id={k[2]};"
            mysql_1.cursor.execute(mysql_1.sql, k)

def insert_update_wei(name, data):
    with Mysql_fun()as mysql_1:
        for k in data:
            placeholders = ', '.join(['%s'] * len(k))  # 生成占位符
            mysql_1.sql = f"insert into {name} values({placeholders}) on duplicate key update mid='{k[3]}';"
            mysql_1.cursor.execute(mysql_1.sql, k)

def m_1(name, num1):
    data_1 = batch_pop(name, num1)
    insert_sql(name, data_1)

def m_wei(name, num1):
    data_1 = batch_pop(name, num1)
    insert_update_wei(name, data_1)

def m_tou(name, num1):
    data_1 = batch_pop(name, num1)
    insert_update_tou(name, data_1)

if __name__ == '__main__':
    m_tou('tou_hot', 50)
    m_1('tou_content', 1000)
    m_1('wei_topic', 50)
    m_wei('wei_hot', 50)
    m_1('wei_content', 1000)
