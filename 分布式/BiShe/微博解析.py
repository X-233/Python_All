import parsel
from urllib.parse import quote

def analysis(html_body):
    selector = parsel.Selector(html_body)
    html = selector.xpath('//div[@action-type="feed_list_item"]')
    data_list = []
    for i in html:
        data_name = i.xpath('.//p[@node-type="feed_list_content"]/@nick-name').get()
        data_url = i.xpath('.//div[@class="from"]/a/@href').get()
        data_home = i.xpath('.//div[@class="avator"]/a/@href').get()
        data_uid = i.xpath('.//div[@class="avator"]/a/@href').re(r'\d+')
        data_content = i.xpath('.//p[@class="txt"][last()]').xpath('string(.)').get()
        data_share = i.xpath('.//div[@class="card-act"]/ul/li[1]').xpath('string(.)').get()
        data_count = i.xpath('.//div[@class="card-act"]/ul/li[2]').xpath('string(.)').get()
        data_like = i.xpath('.//div[@class="card-act"]/ul/li[3]//span/text()').get()
        data_source_url = i.xpath('.//div[@class="avator"]/div[@class="like"]/a/@href').get()
        data_mid = i.xpath('./@mid').get()
        if data_share:
            # 数据字典
            if '万' in data_share:
                data_share = data_share[:-1]
            data = {
                'data_name': data_name,
                'data_url': 'https:' + data_url,
                'data_home': 'https:' + data_home,
                'data_uid': data_uid[0],
                'data_content': data_content,
                'data_share': 0 if '转发' in data_share else int(data_share.strip()),
                'data_count': 0 if '评论' in data_count else int(data_count.strip()),
                'data_like': 0 if '赞' in data_like else int(data_like.strip()),
                'data_source_url': data_source_url,
                'data_mid': data_mid,
            }
            if data['data_count'] > 100:
                data_list.append(data)
    return data_list


# 传入网页json数据(话题榜), 返回字典类型
def analysis_topic(html_json):
    # 获取数据,解析
    for i in html_json:
        try:
            # url = 'https://s.weibo.com/weibo?q=' + quote('#' + i['note'] + '#') + '&topic_ad='
            data = {
                'raw_hot': i['raw_hot'],
                'note': i['note'],
                'mid': i['mid'] if i['mid'] else 0,
                'onboard_time': i['onboard_time'],
                'url': 'https://s.weibo.com/weibo?q=' + i['note'],
            }
            yield data
        except Exception as e:
            print(e)

def get_json(html_json):
    for i in html_json:
        data = {
            'created_at': i['created_at'],
            # 回复数量
            'floor_number': i['floor_number'],
            # 发帖人的uid
            'analysis_extra': i['analysis_extra'],
            'id': i['id'] if i['id'] else 0,
            # 点赞数量
            'like_counts': i['like_counts'],
            # Ip地址
            'user_location': i['user']['location'],
            'text_raw': i['text_raw'],
            # 作者名称
            'user_screen_name': i['user']['screen_name'],
            'user_id': i['user']['id'],
            # 粉丝数量
            'user_followers_count': i['user']['followers_count'],
            # 关注数量
            'user_friends_count': i['user']['friends_count'],
        }
        yield data
