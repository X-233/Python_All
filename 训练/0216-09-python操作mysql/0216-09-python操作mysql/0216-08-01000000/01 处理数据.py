"""
    将 changsha.csv 处理成可以给 sql 直接插入的数据，然后保存到 changsha_result.sql 文件
"""

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

lines = open('changsha.csv', mode='r', encoding='gbk').readlines()

file = open('changsha_result.sql', mode='w', encoding='utf-8')
for line in lines:
    data = tuple(line.strip().split(','))
    sql_format = "insert into changsha(city, region, title, star_level, star, review_num, mean_price, comment_list1, comment_list2, comment_list3, link, shop_tag_cate_click, shop_tag_region_click, addr) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
    try:
        ret = sql_format % data
        print(ret)
        file.write(ret)
        file.write('\n')
    except Exception as e:
        print(e)

file.close()
