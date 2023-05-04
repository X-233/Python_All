show tables;
drop table author;
create table author
(
    id    int primary key auto_increment,
    name  varchar(50) not null,
    phone varchar(11) not null unique,
    hobby varchar(255)
);

drop table article;
create table article
(
    id        int primary key auto_increment,
    title     varchar(255),
    body      text,
    author_id int,
    -- 定义一个外键   外键为 author_id 关键 author 数据表的 id 字段
    -- 外键约束
    constraint fk_author_id foreign key (author_id) references author (id)
);

insert into author
values (1, '烽火戏诸侯', '110110', '吃饭'),
       (2, '我吃西红柿', '110111', '睡觉'),
       (3, '辰东', '110112', '打豆豆');

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

/*
    外键是一种约束,不给外键其实也是可以的
    django orm
    sqlalchemy

    一张表会有一个主键

    表与表之间的关系 -- 外键
*/
-- 根据小说的名字查询作者
select *
from article
where title = '剑来';

select *
from author
where id = 1;

-- 子查询
select *
from author
where id = (select author_id
            from article
            where title = '飞剑问道');