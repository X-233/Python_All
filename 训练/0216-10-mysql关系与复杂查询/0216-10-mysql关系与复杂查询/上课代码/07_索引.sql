select *
from student;

select *
from student
where name = '宋婷';

-- 如果某一个字段经常用于查询,就可以添加一个索引
-- ALTER TABLE 表名字 ADD INDEX 索引名 (列名);
desc student;
show index from student;

ALTER TABLE student
    ADD INDEX idx_name (name);

ALTER TABLE student
    drop INDEX idx_name;
-- 会单独维护一个索引列  查询的时候会有查询算法优化 二分法/二叉树
-- 会单独维护一个索引列 修改的时候会有负担(增删)