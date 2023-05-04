/*
    将 employee.txt 与 salary.txt 的数据插入到数据库
    1. 使用 .sql 创建数据库, 使用约束与外键约束
    2. 使用 .py 脚本将数据插入到数据库

    重复的数据直接跳过
*/
show databases;
drop database company;
create database company character set 'utf8mb4';
use company;

/*
    丁娜,女,1998/12/27,18706012232,532211428@qq.com,北京市海淀区颐和园路5号,342622199801144314
*/

create table employee
(
    id        int primary key auto_increment,
    name      varchar(20),
    gender    char(2),
    birth_day date,
    mobile    char(11),
    email     varchar(50),
    address   varchar(255),
    id_card   char(18)
);
-- 默认是给id 需要补0
insert into employee
values (%s, %s, %s, %s, %s, %s, %s, %s);

/*
丁娜,生产部门,生成主管,5000
*/
create table salary
(
    id          int primary key auto_increment,
    name        varchar(25),
    dept        varchar(25),
    position    varchar(25),
    salary      float,
    employee_id int,
    constraint fk_employee_id foreign key (employee_id) references employee (id)
);

insert into salary values (%s, %s, %s, %s, %s, %s);


select id from employee where name=%s;
select id from employee where name='丁娜';