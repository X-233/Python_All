/*


('刘岩', 50, 2485, '13780795566', '数学'),
('张华', 34, 3707, '13799441431', '数学'),
('王健', 22, 2938, '15055876745', '语文'),
('田丹丹', 51, 3888, '18844659764', '语文'),
('颜秀云', 42, 2148, '18761783434', '数学'),
('胡彬', 38, 3219, '18915977888', '数学'),
('王涛', 24, 2064, '13788639370', '数学'),
('宋琴', 48, 2245, '15208504138', '语文'),
('王杨', 25, 2594, '14568517722', '数学'),
('钟畅', 35, 2710, '14717085283', '语文'),
teacher
id	            员工id
name	        员工名字
age	            年龄
salary	        薪水
phone	        电话号码
in_department	所处部门
*/

show databases;
create database python character set 'utf8mb4';
use python;
drop table teacher;
create table teacher
(
    id            int primary key auto_increment, -- 主键约束
    name          varchar(20)     not null,       -- not null 非空约束
    age           int(3),
    salary        float default 2500,             -- default 默认约束
    phone         char(11) unique not null,       -- unique 唯一约束
    in_department varchar(20)
);

insert into teacher
values (1, '刘岩', 50, 2485, '13780795566', '数学');
-- Duplicate entry '1' for key 'PRIMARY'
-- Duplicate entry 重复输入
-- 主键不能重复
insert into teacher
values (1, '张华', 34, 3707, '13799441431', '数学');


/*非空约束*/
insert into teacher
values (0, '张华', 34, 3707, '13799441431', '数学');


insert into teacher
values (0, null, 22, 2938, '15055876745', '语文');
-- '' 空字符串  null 空内容

insert into teacher(id, age, salary, phone, in_department)
values (0, 22, 2938, '15055876745', '语文');



insert into teacher
values (0, '田丹丹', 51, 3888, '18844659764', '语文');

/*有些内容不填,就使用默认值*/
-- 如果 salary 不填, 默认就是 2500
insert into teacher(id, name, age, phone, in_department)
values (0, '田丹丹', 51, '18844659764', '语文');

insert into teacher(id, name, age, phone, in_department)
values (0, '颜秀云', 42, '18761783434', '数学');


insert into teacher
values (0, '王涛', 24, 2064, '13788639370', '数学'),
       (0, '宋琴', 48, 2245, '15208504138', '语文');

/*
约束可以组合在一起使用
*/