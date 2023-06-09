/*
('丁娜','销售部门','女','1998/12/27','18706012232','532211428@qq.com','北京市海淀区颐和园路5号','342622199801144314'),
('陈伟','生产部门','男','1995/10/25','13459732456','572501101@qq.com','北京市海淀区双清路30号','342622199709066819'),
('曲旭','销售部门','男','1999/1/8','18850840171','582300330@qq.com','上海市杨浦区邯郸路220号','342622199709198176'),
('刘淑珍','销售部门','女','1998/2/4','18650523989','588100505@qq.com','杭州市西湖区余杭塘路866号','342622199708171596'),
('王晶','生产部门','男','1998/4/20','18650795182','598202702@qq.com','上海市杨浦区四平路1239号','342622199711026453'),
('刘红梅','技术部','女','1998/7/20','18759125223','512101504@qq.com','厦门市思明区思明南路422号','320923199806290932'),
('陈秀兰','技术部','男','1999/2/1','18705908359','512501129@qq.com','江苏省南京市鼓楼区汉口路22号','342625199812140158'),
('戴文','技术部','男','1997/1/15','18065178692','512802414@qq.com','重庆市沙坪坝区沙坪坝正街174号','342601199705132151'),
('陈丽','技术部','女','1998/11/29','15260972133','518110817@qq.com','四川省成都市武侯区一环路南一段24号','340223199802050515'),
('冉兵','技术部','男','1997/9/15','13850208664','530300603@qq.com','广州市海珠区新港西路135号','342623199806105732'),
*/

create table employee
(
    id        int primary key auto_increment,
    name      varchar(50)           not null,
    dept_name varchar(20)           null default '培训中心',
    gender    enum ('男', '女', '其他') not null,
    birth     date                  not null,
    mobile    char(11)              not null unique,
    email     varchar(255)          null,
    address   varchar(255)          null,
    id_card   char(18)              not null unique comment '身份证号码'
);

insert into employee(name, dept_name, gender, birth, mobile, email, address, id_card)
values ('丁娜', '销售部门', '女', '1998/12/27', '18706012232', '532211428@qq.com', '北京市海淀区颐和园路5号', '342622199801144314'),
       ('陈伟', '生产部门', '男', '1995/10/25', '13459732456', '572501101@qq.com', '北京市海淀区双清路30号', '342622199709066819'),
       ('曲旭', '销售部门', '男', '1999/1/8', '18850840171', '582300330@qq.com', '上海市杨浦区邯郸路220号', '342622199709198176'),
       ('刘淑珍', '销售部门', '女', '1998/2/4', '18650523989', '588100505@qq.com', '杭州市西湖区余杭塘路866号', '342622199708171596'),
       ('王晶', '生产部门', '男', '1998/4/20', '18650795182', '598202702@qq.com', '上海市杨浦区四平路1239号', '342622199711026453'),
       ('刘红梅', '技术部', '女', '1998/7/20', '18759125223', '512101504@qq.com', '厦门市思明区思明南路422号', '320923199806290932'),
       ('陈秀兰', '技术部', '男', '1999/2/1', '18705908359', '512501129@qq.com', '江苏省南京市鼓楼区汉口路22号', '342625199812140158'),
       ('戴文', '技术部', '男', '1997/1/15', '18065178692', '512802414@qq.com', '重庆市沙坪坝区沙坪坝正街174号', '342601199705132151'),
       ('陈丽', '技术部', '女', '1998/11/29', '15260972133', '518110817@qq.com', '四川省成都市武侯区一环路南一段24号', '340223199802050515'),
       ('冉兵', '技术部', '男', '1997/9/15', '13850208664', '530300603@qq.com', '广州市海珠区新港西路135号', '342623199806105732');


/*
pymysql 事务操作回滚
*/