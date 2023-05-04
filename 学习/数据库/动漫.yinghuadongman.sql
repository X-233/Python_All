show databases ;

use 阿里云;

show tables ;

create table 动漫(
    id int primary key auto_increment,
    url varchar(255) not null default '',
    dm_name varchar(255) not null default '',
    score decimal(2, 1) default 0.0,
    img varchar(255) not null default '',
    time_1 datetime,
    seed text
);

drop table if exists 动漫;
delete from 动漫;

select * from 动漫;

select * from 动漫 ORDER BY score desc limit 100;


