use python;
create database students character set 'utf8mb4';
use students;
create table student
(
    id      integer primary key auto_increment,
    name    varchar(255),
    chinese Float,
    math    Float,
    english Float
);