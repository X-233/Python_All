use python;

create table author
(
    id    int primary key auto_increment,
    name  varchar(50) not null,
    phone varchar(11) not null unique,
    hobby varchar(255)
);

create table article
(
    id        int primary key auto_increment,
    title     varchar(255),
    body      text,
    author_id int
);

insert into author
values (1, '烽火戏诸侯', '110110', '吃饭'),
       (2, '我吃西红柿', '110111', '睡觉'),
       (3, '辰东', '110112', '打豆豆');

insert into author
values (4, '正心', '110119', '写代码');

-- 插入的时候外键不存在
insert into article
values (1, '剑来', '...', 1),
       (2, '雪中悍刀行', '...', 1),
       (3, '星辰变', '...', 2),
       (4, '沧元图', '...', 2),
       (5, '飞剑问道', '...', 2),
       (6, '圣墟', '...', 3),
       (7, '遮天', '...', 3),
       (8, '完美世界', '...', 3);

insert into article
values (9, 'python开发', '...', 5);

-- 内联结
select article.id, title, body, name, phone, hobby
from article
         inner join author
                    on article.author_id = author.id;


-- 左联结
select article.id, title, body, name, phone, hobby
from article
         left join author
                   on article.author_id = author.id;

-- 右联结
select article.id, title, body, name, phone, hobby
from article
         right join author
                    on article.author_id = author.id;


# select a.id, name, subject, office, teacher_name
# from association a
#          inner join student s on a.student_id = s.id
#          inner join teacher t on a.teacher_id = t.id
# where teacher_name = '张三'
# ;

-- 联结查询之后可以继续筛选