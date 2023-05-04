import pymysql

connection = pymysql.connect(host='81.68.68.240', user='windows', password='Zhengxin...123456', database='python',
                             port=3306)
cursor = connection.cursor()

with open('student.txt', mode='r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:  # 第七条数据会报错
    try:
        student = tuple(line.strip().split(','))
        insert_sql_template = "insert into student(no, name, gender, birth, phone, email, address, id_card)values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
        print(insert_sql_template % student)
        cursor.execute(insert_sql_template % student)
        # connection.commit()  # 每次插入都会进行提交 第七条数据会出错
    except Exception as e:
        # 回滚 可以把之前的操作撤销
        connection.rollback()
        print("出错啦", e)

connection.commit()
cursor.close()
connection.close()
"""
    撤销更改, 把没有 commit 的操作全部撤销
    
    try:
        张三给李四转钱
            1. 张三账户金额减 100
            2. 李四账户金额加 100
            3. 在交易记录表新增一条记录 
        三步操作是一个整体,必须一起成功
    exception 
        rollback 出现异常撤销交易
"""
