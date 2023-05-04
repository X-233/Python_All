/*  注释
    1. 在本地数据库服务器中创建一个属于自己的数据库：python（期数-作业次数-学号）
    2. 选择数据库后创建一张 changsha 数据表，字段参考 `01 处理数据.py` 文件
    3. 将处理后的 changsha_result.csv 数据插入到数据库
*/

use python;

create table changsha
(
    id                    integer not null auto_increment primary key,
    city                  varchar(255),
    region                varchar(255),
    title                 varchar(255),
    star_level            varchar(255),
    star                  varchar(255),
    review_num            int,
    mean_price            varchar(255),
    comment_list1         float,
    comment_list2         float,
    comment_list3         float,
    link                  varchar(255),
    shop_tag_cate_click   varchar(255),
    shop_tag_region_click varchar(255),
    addr                  varchar(255)
);

insert into changsha(city, region, title, star_level, star, review_num, mean_price, comment_list1, comment_list2, comment_list3, link, shop_tag_cate_click, shop_tag_region_click, addr) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
