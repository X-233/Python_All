import pymysql

connection = pymysql.connect(host='81.68.68.240', user='windows', password='Zhengxin...123456', database='python',
                             port=3306)
cursor = connection.cursor()

with open('student.txt', mode='r', encoding='utf-8') as f:
    lines = f.readlines()
insert_sql_template = "insert into student(no, name, gender, birth, phone, email, address, id_card)values (%s, %s, %s, %s, %s, %s, %s, %s);"
data_list = []
for line in lines:
    try:
        student = tuple(line.strip().split(','))
        data_list.append(student)
        # cursor.execute(insert_sql_template, student)  # 执行了 43 次插入
    except Exception as e:
        # connection.rollback()
        print("出错啦", e)

cursor.executemany(insert_sql_template, data_list)

for data in data_list:
    cursor.execute(insert_sql_template, data)

connection.commit()
cursor.close()
connection.close()

"""
    pymysql 是 mysql 驱动, 作用是用来链接服务器,执行原生的 sql
    原生的 sql 建议在 .sql 文件里面编写
    
    参数化与
"""