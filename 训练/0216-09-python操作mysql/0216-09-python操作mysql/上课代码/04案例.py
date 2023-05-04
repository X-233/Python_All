"""将上节课的作业插入到服务器"""
import pymysql

connection = pymysql.Connection(
    user='windows', password='Zhengxin...123456',
    host='81.68.68.240', port=3306,
    database='python')
cursor = connection.cursor()

fieldnames = ['city',  # 城市
              'region',  # 行政区
              'title',  # 门店名称
              'star_level',  # 星级
              'star',  # 星级得分
              'review_num',  # 点评总数
              'mean_price',  # 人均消费
              "comment_list1",  # 口味
              "comment_list2",  # 环境
              "comment_list3",  # 环境
              "link",  # 链接网址
              "shop_tag_cate_click",  # 分类
              "shop_tag_region_click",  # 商圈
              "addr",  # 详细地址
              ]

lines = open('../0216-08-01000000/changsha.csv', mode='r', encoding='gbk').readlines()
sql_format = "insert into changsha(city, region, title, star_level, star, review_num, mean_price, comment_list1, comment_list2, comment_list3, link, shop_tag_cate_click, shop_tag_region_click, addr) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

for line in lines:
    data = tuple(line.strip().split(','))
    try:
        cursor.execute(sql_format, data)
    except Exception as e:
        print(e)
    # connection.commit()  # 执行一次 sql 提交一次

connection.commit()  # 最后一起提交
cursor.close()
connection.close()
