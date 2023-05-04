import pymysql
import json


class Student:
    """学生信息类"""

    def __init__(self, name, chinese, math, english):
        """
        :param name: 姓名
        :param chinese: 语文成绩
        :param math: 数学成绩
        :param english: 英语成绩
        """
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    @property
    def total(self):
        return self.chinese + self.math + self.english


class StudentsDB:
    """学生数据模型"""

    def __init__(self):
        self.connection = pymysql.connect(
            host='81.68.68.240', user='windows',
            password='Zhengxin...123456', database='students',
            port=3306)
        self.cursor = self.connection.cursor()

    def insert(self, student):
        """
        增加学员信息的方法
        :param student: 字典格式的学生信息
        :return:
        """
        data = (0, student['name'], student['chinese'], student['math'], student['english'])
        insert_sql = 'INSERT INTO student values (%s, %s, %s, %s, %s)'
        self.cursor.execute(insert_sql, data)
        self.connection.commit()

    def delete(self, student):
        """删除学生的方法"""
        pass

    def search(self, name):
        """
        指定姓名查询学生信息
        :param name: 学员姓名
        :return: 学员信息 or None
        """
        pass

    def change(self, stu):
        """
        修改学员信息
        :param stu: 需要修改的学员名字
        :return: 修改成功返回True; 不成功返回False
        """
        pass


# 实例化数据模型
db = StudentsDB()
data = open('students.json', mode='r', encoding='utf-8').read()

stu_list = json.loads(data)
for stu in stu_list:
    db.insert(stu)
