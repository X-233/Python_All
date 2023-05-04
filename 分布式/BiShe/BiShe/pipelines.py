import json
from 数据库方法 import Redis_fun
from .items import WeiItem, Wei_contentItem

class TouPipeline:
    def __init__(self):
        self.redis_link = Redis_fun()
        # if spider.name == 'tou':
        #     self.redis_link.set_ttl('tou_hot', 600)
        # if spider.name == 'tou_hot':
        #     pass

    def process_item(self, item, spider):
        if spider.name == 'tou':
            print(item)
            self.redis_link.push_list_data('tou_hot', json.dumps(dict(item)))
            self.redis_link.push_list_data('tou_hot_list', json.dumps({'url': dict(item)['Id']}))
            # self.redis_link.push_set_data('tou_set', json.dumps(dict(item)))
            # self.redis_link.push_hash_data('tou_hash', dict(item))
        if spider.name == 'tou_hot':
            print(item)
            self.redis_link.push_list_data('tou_content', json.dumps(dict(item)))
        return item

    def close_spider(self, spider):
        self.redis_link.conn.close()

class WeiPipeline:
    def __init__(self):
        self.redis_link = Redis_fun()
        # if spider.name == 'wei':
        #     self.redis_link.set_ttl('wei_hot', 600)

    def process_item(self, item, spider):
        if spider.name == 'wei':
            print(item)
            self.redis_link.push_list_data('wei_hot', json.dumps(item))
            self.redis_link.push_list_data('wei_hot_list', json.dumps({'url': item['url']}))

        if spider.name == 'wei_content':
            if type(item) is WeiItem:
                print(dict(item))
                self.redis_link.push_list_data('wei_topic', json.dumps(dict(item)))
            if type(item) is Wei_contentItem:
                print(dict(item))
                self.redis_link.push_list_data('wei_content', json.dumps(dict(item)))
        return item

    def close_spider(self, spider):
        self.redis_link.conn.close()

