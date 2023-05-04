drop database python;
create database python character set 'utf8mb4';

use python;
show tables;
create table student
(
    id      int primary key auto_increment,
    name    varchar(25),
    subject varchar(25)
);

create table teacher
(
    id           int primary key auto_increment,
    office       varchar(25),
    teacher_name varchar(25)
);

create table association
(
    id         int primary key auto_increment,
    student_id int,
    teacher_id int
    /*
    ,
    constraint fk_student_id foreign key (student_id) references student (id),
    constraint fk_teacher_id foreign key (teacher_id) references teacher (id)
    */
);
insert into student
values (1, '小红', '文科'),
       (2, '小绿', '文科'),
       (3, '小灰', '理科'),
       (4, '小黑', '理科')
;

insert into teacher
values (1, '语文老师', '张三'),
       (2, '历史老师', '李四'),
       (3, '物理老师', '王五')
;

insert into association
values (1, 1, 1),
       (2, 1, 2),
       (3, 2, 1),
       (4, 2, 2),
       (5, 3, 1),
       (6, 3, 3),
       (7, 4, 1),
       (8, 4, 3)
;

-- 张三老师带了哪些学生
-- 1. 查询老师的信息
select *
from teacher
where teacher_name = '张三';
-- 2. 到关系表查找学生的 id
select *
from association
where teacher_id = 1;
-- 3. 找到对应的学生
select *
from student
where id in (1, 2, 3, 4);


select *
from student
where id in (select student_id
             from association
             where teacher_id = (select id
                                 from teacher
                                 where teacher_name = '李四'));

