"""
参考 db.py 的逻辑
 + 保留原来的方法，将方法里面的逻辑改成数据库的
 + 新增根据指定科目的成绩大于某个分数的查询的方法（例如：语文分数大于60份的学员）
 + 新增总分大于多少分的查询
"""
import pymysql


class MysqlStudentDb:
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            database='python'
        )
        self.cursor = self.conn.cursor()

    def insert(self, student):
        """将学生数据插入到列表"""
        sql = '''insert into student(name, chinese, math, english) values (%s, %s, %s, %s)'''
        self.cursor.execute(sql, (student["name"], student["chinese"], student["math"], student["english"]))
        self.conn.commit()

    def all(self):
        self.cursor.execute('select * from student;')
        return self.cursor.fetchall()

    def search_by_name(self, name):
        sql = 'select * from student where name=%s;'
        self.cursor.execute(sql, (name,))
        return self.cursor.fetchall()


db = MysqlStudentDb()
print(db.all())
# db.insert({"name": "张三", "math": "65", "chinese": "75", "english": "100"})
# print(db.all())
print(db.search_by_name('李玉珍'))
