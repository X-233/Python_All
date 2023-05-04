import pymysql


class StudentDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host='81.68.68.240', user='windows',
            password='Zhengxin...123456', database='python',
            port=3306)
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def find_student_by_name(self, name):
        sql = "SELECT * FROM student WHERE name = %s"
        self.cursor.execute(sql, (name,))
        return self.cursor.fetchall()

    def find_student_by_id(self, sid):
        sql = "SELECT * FROM student WHERE id = %s"
        self.cursor.execute(sql, (sid,))
        return self.cursor.fetchone()


db = StudentDB()
# name = input('请输入学生姓名:')
# ret = db.find_student_by_name(name)
# print(ret)
print(db.find_student_by_id(10))

db.close()  # 程序运行完了之后需要关闭与数据库的链接
"""
一般使用pymysql开发的时候都是使用面向对象进行封装

ORM 关系模型对象
"""
