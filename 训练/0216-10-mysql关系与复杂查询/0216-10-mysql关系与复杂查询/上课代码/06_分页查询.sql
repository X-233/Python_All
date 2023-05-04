drop database python;
create database python character set 'utf8mb4';

use python;
drop table student;
create table student
(
    id      int primary key auto_increment,
    name    char(3),
    chinese float,
    math    float,
    english float
);

insert into student(name, chinese, math, english)
values ('胡秀英', 77, 75, 51),
       ('李玉珍', 58, 40, 72),
       ('王超', 78, 96, 56),
       ('宋婷', 99, 64, 84),
       ('吴桂香', 75, 92, 43),
       ('范鹏', 94, 93, 95),
       ('钟淑兰', 70, 80, 46),
       ('刘桂芝', 49, 59, 94),
       ('王畅', 66, 64, 96),
       ('谢秀华', 78, 63, 59),
       ('王宇', 59, 66, 94),
       ('陈兰英', 67, 44, 71),
       ('杜刚', 44, 82, 92),
       ('鲁超', 62, 85, 59),
       ('陈静', 53, 51, 81),
       ('郑玉梅', 51, 72, 57),
       ('郭丹丹', 40, 44, 81),
       ('李玉兰', 94, 68, 74),
       ('高刚', 95, 89, 74),
       ('张成', 96, 52, 78);


-- 分页查询

select *
from student;

-- 一页 5 条数据, 查询第一页
-- limit (page-1)*count,count
select *
from student
limit 0, 5;

select *
from student
limit 5, 5;


-- page=3 count=5
select *
from student
limit 10, 5;

-- 过滤三门科目只要有一门科目没有合格的学员
select *
from student
where chinese < 60
UNION
select *
from student
where math < 60
UNION
select *
from student
where english < 60;