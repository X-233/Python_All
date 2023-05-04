use python;
-- 有了学号,还有必要用 id 吗?
truncate student;
create table student
(
    id      int primary key auto_increment, -- id
    no      char(6),                        -- 学号
    name    varchar(20),                    -- 名字
    gender  char(1),                        -- 性别
    birth   date,                           -- 出生日期
    phone   char(11),                       -- 电话号码
    email   varchar(50),                    -- 邮箱
    address text,                           -- 地址
    id_card char(18)                        -- 身份证号码
);

-- 插入语句
insert into student(no, name, gender, birth, phone, email, address, id_card)
values ('319001', '赵一', '男', '1998/12/27', '18706012232', '532211428@qq.com', '北京市海淀区颐和园路5号', '342622199801144314');

truncate student;
select * from student;
select * from student where birth>'1998-04-20';


create table students2(
    id int primary key auto_increment,
    name varchar(50),
    math float,
    chinese float,
    english float
);

insert into students2(name, math, chinese, english) value (%s,%s,%s,%s);
select * from students2;
delete from students2 where name=%s;
update students2 set name='' where name=%s;