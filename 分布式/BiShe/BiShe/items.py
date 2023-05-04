# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TouItem(scrapy.Item):
    # define the fields for your item here like:
    hot_ranking: int = scrapy.Field()
    Title: str = scrapy.Field()
    Url: str = scrapy.Field()
    Id: int = scrapy.Field()
    HotValue: int = scrapy.Field()
    source_id: int = scrapy.Field()

class TouContentItem(scrapy.Item):
    # define the fields for your item here like:
    user_name: str = scrapy.Field()
    user_id: int = scrapy.Field()
    text: str = scrapy.Field()
    source_id: int = scrapy.Field()
    open_url: str = scrapy.Field()

class WeiItem(scrapy.Item):
    data_name = scrapy.Field()
    data_url = scrapy.Field()
    data_home = scrapy.Field()
    data_uid = scrapy.Field()
    data_content = scrapy.Field()
    data_share: int = scrapy.Field()
    data_count: int = scrapy.Field()
    data_like: int = scrapy.Field()
    data_source_url: int = scrapy.Field()
    data_mid: int = scrapy.Field()


class Wei_contentItem(scrapy.Item):
    """
    :param craeated_at: 时间
    """
    created_at = scrapy.Field()
    floor_number = scrapy.Field()
    analysis_extra = scrapy.Field()
    id = scrapy.Field()
    like_counts = scrapy.Field()
    text_raw = scrapy.Field()
    data_uid = scrapy.Field()
    user_location = scrapy.Field()
    user_screen_name = scrapy.Field()
    user_id = scrapy.Field()
    user_followers_count = scrapy.Field()
    user_friends_count = scrapy.Field()