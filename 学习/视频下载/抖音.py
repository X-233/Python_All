import requests
import parsel

class Request:

    def __init__(self):
        self.url = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'Cookie': 'ttwid=1|y_CvvcqvxXiLYrJz_P7B58lLJP8DI0zpNtMjYiEfsZ4|1683366650|895496b5d34ed598ae2fadc4eb60f29dfabc12bb97f742aade06c7a5f41b4f73; douyin.com; strategyABtestKey="1683366652.702"; passport_csrf_token=07a8b28d8995d34709faf8358e44daf0; passport_csrf_token_default=07a8b28d8995d34709faf8358e44daf0; s_v_web_id=verify_lhbt1ifl_7u22bSnh_ynQk_42Uz_83BB_0DrWNHVMTvil; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNzciI6Ii0tLS0tQkVHSU4gQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbk1JSUJEakNCdFFJQkFEQW5NUXN3Q1FZRFZRUUdFd0pEVGpFWU1CWUdBMVVFQXd3UFltUmZkR2xqYTJWMFgyZDFcclxuWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUWNEUWdBRTdOMUpRRHN3TkRPK1ZzR0YrQnU2eE5ES1xyXG5MMW42MkoyNUl5SDV6dENyWFJYRWRsb0VhYTdWSFgrK2F6T2RMOG54aWJWVmNvSjY5ZGFma0h3eWVVc0xPS0FzXHJcbk1Db0dDU3FHU0liM0RRRUpEakVkTUJzd0dRWURWUjBSQkJJd0VJSU9kM2QzTG1SdmRYbHBiaTVqYjIwd0NnWUlcclxuS29aSXpqMEVBd0lEU0FBd1JRSWdmTDA4bVVVdmgzS3NKS3NHK3lhc3hUM3Mzd3FFQzRIQmhuNHNGVU9SZllzQ1xyXG5JUURjN3FzT2MxcG8venZIQ25HU3AweHlyZTJDMW1GaCt3MGFIeko3K1R6UmdRPT1cclxuLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbiJ9; ttcid=eca62620876e4c958458fffbcf200d2542; csrf_session_id=09f89565f8395d10942b65761d1abf9a; VIDEO_FILTER_MEMO_SELECT={"expireTime":1683971705018,"type":1}; download_guide="3/20230506"; pwa2="3|0"; msToken=EexSAmjEIhuFF52YWXhP5YtoRvlpNoB-BbDp0JvkFiHewD3Vtn1EbO8wvy-a1_Eu59vt9dqLYkMmny23zOSovvwww82-AZXtbepDkn40LSX4pyFOLWdxwqAH9kOQEQ==; __ac_nonce=064562c9a0051c02c23ac; __ac_signature=_02B4Z6wo00f01DUT7EgAAIDAtREWC-PXVVg1M-jAAGkZEobTmt1DsMcYI4.A2yK83ZWFYKhSNafnWgzd0Fm7P43060WIv4sPa3f.MaDOiQuyr4aXFdL7XXnC92H0wHXYKWKXxocmsLJ0rVcC1c; home_can_add_dy_2_desktop="1"; msToken=zzouRavWhK2wJjYl9Q0yiFFTC35ZyP-7xvXFb7PNPVwZG0-Olwcds-KOCQnbG5URjcKHF6x0-Kstej7-sBl9TGxBxEhq61fDiZDY1Ox7sH14vJPH5Bro; tt_scid=GJd84LbbKkf-wHijSDjUiJQp7k.CtLJH6BamzwhhIDIqiIylvRlafO.dIt89.fg9398e',
        }
        self.data = ''
        self.params = {
            'keyword': '寿司的做法教程',
            # 'search_source': 'search_bar_inner',
            # 'query_correct_type': '1',
            # 'is_filter_search': '0',
            # 'from_group_id': '7224138552559406395',
            'offset': '0',
            'count': '10',
            # 'pc_client_type': '1',
            # 'version_code': '190600',
            # 'version_name': '19.6.0',
            # 'cookie_enabled': 'true',
            # 'screen_width': '1596',
            # 'screen_height': '1064',
            # 'browser_language': 'zh-CN',
            # 'browser_platform': 'Win32',
            # 'browser_name': 'Chrome',
            # 'browser_version': '112.0.0.0',
            # 'browser_online': 'true',
            # 'engine_name': 'Blink',
            # 'engine_version': '112.0.0.0',
            # 'os_name': 'Windows',
            # 'os_version': '10',
            # 'cpu_core_num': '8',
            # 'device_memory': '8',
            # 'platform': 'PC',
            # 'downlink': '10',
            # 'effective_type': '4g',
            # 'round_trip_time': '50',
            # 'webid': '7230004666687768122',
            # 'msToken': '_xjDGZPT3H700pXy00FQUyjKEpWxFvnUKXvW6mamKt9L8bBxxWDNkIG_XvWt-egNz7fLkRs7i7A2nbOu4d94KEu-6k0-0UEAWVibdfZbwRaHdFpYHIymGw==',
            'X-Bogus': 'DFSzswVOJxJANtbvtCQpVM9WX7Jr',
        }
        self.ip = ''
        self.json = ''
        self.urls = ''

    @staticmethod
    def dct(func):
        def wrapper(*args, **kwargs):
            resp, tag = func(*args, **kwargs)
            if tag == 'get_text':
                print('是get_text类型')
                return resp
            if tag == 'get_content':
                print('是get_content类型')
                return resp
            if tag == 'get_json':
                print('是get_json类型')
                return resp
            if tag == 'post_json':
                print('是post_json类型')

        return wrapper

    @dct
    def get_text(self):
        resp = requests.get(url=self.url, headers=self.headers).text
        select = parsel.Selector(resp)
        return select, 'get_text'

    @dct
    def get_content(self):
        resp = requests.get(url=self.url, headers=self.headers).content
        return resp, 'get_content'

    @dct
    def get_json(self):
        resp = requests.get(url=self.url, headers=self.headers, params=self.params)
        print(resp.status_code)
        resp = resp.json()
        return resp, 'get_json'

    @dct
    def post_json(self):
        resp = requests.post(self.url, headers=self.headers, data=self.data, json=self.json).json()
        return resp, 'post_json'


if __name__ == '__main__':
    # data = Request()
    # data.url = 'https://www.douyin.com/hot?modal_id=7229655327011065147'
    # select_1 = data.get_text()
    # data_1 = unquote(select_1.css('#RENDER_DATA::text').get())
    #
    # print(data_1)
    # data_2 = re.findall('//v26(.*?)', data_1)
    # print(data_2)

    data = Request()
    # data.url = 'https://www.douyin.com/search/%E5%AF%BF%E5%8F%B8%E7%9A%84%E5%81%9A%E6%B3%95%E6%95%99%E7%A8%8B'

    # select_2 = data.get_text()
    # title = select_2.css('title::text').get()

    data.url = 'https://www.douyin.com/aweme/v1/web/general/search/single/'
    json_data = data.get_json()
    print(json_data)

