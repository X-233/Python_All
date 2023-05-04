show databases;

use 毕设;

show tables;

create table daxue(
    id int auto_increment primary key,
    school_name varchar(30) not null,
    province_id varchar(30) not null,
    local_province_name varchar(50) not null,
    year_1 varchar(20) not null,
    local_batch_name varchar(40) default null,
    zslx_name varchar(40) default null,
    min_and_min_section varchar(30) default null,
    proscore int default null,
    sg_info varchar(40) default null
);

drop table daxue;

select * from daxue;
