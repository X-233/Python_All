import pymysql

connection = pymysql.Connection(user='windows', password='Zhengxin...123456', host='81.68.68.240', port=3306,
                                database='python')
cursor = connection.cursor()

# 数据库数据表的定义/修改语句用 pymysql 执行吗 ?
# 能执行,但是不推荐  定义/修改语句只要执行一次就可以了

"""执行sql实现增删改查"""
data1 = (0, 'r510vc 15.6英寸笔记本', '笔记本', '华硕', '3399', '', '')

# pymysql 的作用是执行编写好的 sql 语句
sql_format = "insert into goods values ('%s', '%s', '%s', '%s', '%s', '%s', '%s');"
sql = sql_format % data1  # 核心编程 基本数据类型 字符串 字符串的三个格式化方式
print(sql)
cursor.execute(sql)  # 执行 sql

connection.commit()  # 提交更改

# phpstudy pro 不需要提交也会保存修改
cursor.close()
connection.close()
