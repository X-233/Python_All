select article.id, title, body, name, phone, hobby
from article
         inner join author
                    on article.author_id = author.id;

-- 视图是一张虚拟表
create view v_temp(v_id, v_title, v_body, v_name, v_phone, v_hobby) as
select article.id, title, body, name, phone, hobby
from article
         inner join author
                    on article.author_id = author.id;

select * from v_temp;