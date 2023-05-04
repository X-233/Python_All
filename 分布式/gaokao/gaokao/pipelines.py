from 配置文件1 import Mysql_fun

class GaokaoPipeline:
    def __init__(self):
        self.mysql_fun = Mysql_fun()
        self.num_1 = 0
        self.num_2 = []

    def process_item(self, item, spider):
        line = [0, item['school_name'],  item['province_id'], item['local_province_name'], item['year'], item['local_batch_name'], item['zslx_name'], item['min_and_min_section'], item['proscore'], item['sg_info']]
        # self.ws.append(line)
        # self.wb.save('data.xlsx')
        self.num_1 += 1
        self.num_2.append(tuple(line))
        print('*' * 30)
        print(self.num_1)
        if self.num_1 % 10 == 0:
            print(self.num_2)
            self.mysql_fun.sql = "insert into daxue values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            self.mysql_fun.cursor.executemany(self.mysql_fun.sql, self.num_2)
            self.mysql_fun.conn.commit()
            self.num_2 = []
            self.num_1 = 0
        print('*'*30)
        return item

    def close_spider(self, spider):
        self.mysql_fun.conn.close()
