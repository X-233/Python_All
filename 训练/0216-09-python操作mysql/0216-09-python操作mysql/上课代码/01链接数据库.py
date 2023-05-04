# 0. 导入 pymysql 驱动
import pymysql

# 1. 链接数据库
connection = pymysql.Connection(
    user='root',  # 用户名
    password='root',  # 密码
    host='127.0.0.1',  # 本地的数据库
    database='python',  # 指定数据库
    port=3306  # 端口
)

print('链接对象', connection)
# 2. 获取游标对象 (执行sql指令)
cursor = connection.cursor()

# 3. 执行sql语句
sql = 'show databases;'
count = cursor.execute(sql)
print('执行sql之后,受影响的行数:', count)

# 4. 获取执行结果
print(cursor.fetchall())

# 5. 关闭链接对象
cursor.close()
connection.close()
