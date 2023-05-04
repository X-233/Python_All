import pymysql

connection = pymysql.Connection(
    user='windows', password='Zhengxin...123456',
    host='81.68.68.240', port=3306,
    database='python')
cursor = connection.cursor()

# 数据库数据表的定义/修改语句用 pymysql 执行吗 ?
# 能执行,但是不推荐  定义/修改语句只要执行一次就可以了

"""执行sql实现增删改查"""
data1 = (0, 'y400n 14.0英寸笔记本电脑', '笔记本', '联想', '4999', '', '')

# sql_format = "insert into goods values ('%s', '%s', '%s', '%s', '%s', '%s', '%s');"
# sql = sql_format % data1   # 字符串拼接
# cursor.execute(sql)

# 参数化提交
sql_format = "insert into goods values (%s, %s, %s, %s, %s, %s, %s);"
# sql = sql_format % data1
cursor.execute(sql_format, data1)

connection.commit()
cursor.close()
connection.close()
