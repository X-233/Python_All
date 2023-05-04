import logging
import parsel

'''
    头条解析
'''

def tou_hot(json_data):
    for i in json_data['data']:
        data = {
            'Id': 'https://item_id=' + i['ClusterIdStr'],
            'source_id': int(i['ClusterIdStr']),
            'Title': i['Title'],
            'Url': i['Url'],
            'HotValue': i['HotValue'],
        }
        yield data

def tou_content(json_data):
    for i in json_data['data']:
        try:
            x = i['comment']['source']['open_url']
        except Exception as e:
            x = ''
            print(logging.error('这里是错误信息\t' + str(e)))

        data = {
            'user_name': i['comment']['user_name'],
            'user_id': i['comment']['user_id'],
            'text': i['comment']['text'],
            'open_url': x,
        }
        yield data
