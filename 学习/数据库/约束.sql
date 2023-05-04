show databases;

use python;

show tables;

create table bads
(
    id     int primary key auto_increment,
    name   varchar(255)          not null,
    gender enum ('男', '女', '其它') not null,
    age    int                   not null,
    email  varchar(255)          null
);

/*外键约束*/
create table bads
(
    id     int primary key auto_increment
);

select * from bads;

show databases ;

use 毕设;

show tables;
show databases ;
create database 测试 character set 'utf8mb4';

show tables;
drop table student;

create table student(
    id int primary key auto_increment,
    name varchar(12) not null ,
    subject varchar(12) not null
);



drop table if exists teacher;
create table teacher(
    id int primary key auto_increment,
    name varchar(12) not null ,
    type varchar(12) not null ,
    subject varchar(12) not null
);


create table ids(
    id int primary key auto_increment,
    id_stu int
);

show tables;

desc ids;

select * from ids;
select * from student;

drop table student;

insert into student
values
    (1, '张1', '文科'),
    (2, '张2', '理科') ,
    (3, '张3', '文科');

show tables;
select * from teacher;
insert into teacher
values
    (1,'里1', '语文', '文科'),
    (2, '里2', '语文', '理科'),
    (3, '里3', '数学', '文科'),
    (4, '里4', '数学', '理科'),
    (5, '里5', '历史', '文科');

insert into ids
values
    ('');