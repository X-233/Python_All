show databases ;
use 毕设;

show tables;

drop table if exists daxue, ids, teacher, wei_tiezi, wei_topic,student;

create table wei_content(
    id int not null primary key auto_increment,
    created_at varchar(30) not null,
    floor_number int,
    analysis_extra varchar(50),
    mid numeric(25, 0),
    like_counts numeric(12, 0),
    user_location varchar(20),
    text_raw text,
    user_screen_name varchar(40),
    user_id numeric(25, 0),
    user_followers_count int,
    user_friends_count int
);


create table wei_topic(
    id int not null auto_increment primary key,
    data_name varchar(30) not null,
    data_url varchar(255) not null,
    data_home varchar(255),
    data_uid numeric(25, 0) not null,
    data_content text,
    data_share numeric(12, 0),
    data_count numeric(12, 0),
    data_like numeric(12, 0),
    data_source_url varchar(255),
    data_mid numeric(25, 0)
);


create table wei_hot(
    id int not null auto_increment primary key,
    raw_hot int not null,
    note varchar(100) not null,
    mid numeric(25, 0) default 0 not null,
    onboard_time varchar(20) not null,
    url varchar(255)
);

show tables ;

create table tou_hot(
    id int not null auto_increment primary key,
    Ids varchar(50) not null,
    source_id numeric(25, 0) default 0 not null ,
    Title varchar(100) not null,
    Url text not null,
    HotValue int not null
);


create table tou_content
(
    id int not null auto_increment primary key,
    user_name varchar(20) not null,
    user_id numeric(25, 0) not null,
    texts text not null,
    open_url varchar(255),
    source_id numeric(25, 0)
);

drop table wei_hot;
drop table tou_hot;
drop table tou_content;
drop table if exists wei_topic;
drop table wei_content;

select * from tou_hot;
select * from wei_hot;
