import pymysql

connection = pymysql.connect(host='81.68.68.240', user='windows', password='Zhengxin...123456', database='python',
                             port=3306)

# 执行 sql 指令
cursor = connection.cursor()

sql_format = 'select * from student where name =%s;'
sql_format2 = "select * from student where name ='%s';"

name = input('请输入需要查询的学生名字:')

sql = sql_format2 % name  # 字符串拼接可能会导致 sql 注入
print(sql)
cursor.execute(sql)

# 参数化让 pymysql 进行拼接
# cursor.execute(sql_format, (name,))  # 参数化可以解决sql注入
for item in cursor.fetchall():
    print(item)
cursor.close()
connection.close()
