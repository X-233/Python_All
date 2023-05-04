import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='company')
cursor = conn.cursor()

# with open('employee.txt', mode='r', encoding='utf-8') as file:
#     text = file.read()
# lines = text.split()
# employee_insert_sql = 'insert into employee values (%s, %s, %s, %s, %s, %s, %s, %s);'
# for line in lines:
#     data = line.split(',')
#     data = (0, *data)
#     print(data)
#     cursor.execute(employee_insert_sql, data)

salary_inset_sql = 'insert into salary values (%s, %s, %s, %s, %s, %s);'
with open('salary.txt', mode='r', encoding='utf-8') as file:
    text = file.read()
lines = text.split()
search_id_sql = 'select id from employee where name=%s;'
for line in lines:
    # 用户的 id 在哪里有 ？
    data = line.split(',')
    name = data[0]
    cursor.execute(search_id_sql, (name,))
    employee_id = cursor.fetchone()
    data = (0, *data, *employee_id)
    cursor.execute(salary_inset_sql, data)
conn.commit()
cursor.close()
conn.close()
