import pymysql

connection = pymysql.connect(host='81.68.68.240', user='windows', password='Zhengxin...123456', database='python',
                             port=3306)

# 执行 sql 指令
cursor = connection.cursor()

# 1. 准备需要执行的 sql
sql = 'select * from student;'
# 2. 执行 sql --> 返回的结果是一个生成器
cursor.execute(sql)
# 3. 获取查询结果
print('获取一条数据：', cursor.fetchone())
print('获取多条数据：', cursor.fetchmany(2))
print('获取所有数据：', cursor.fetchall())

cursor.close()
connection.close()
