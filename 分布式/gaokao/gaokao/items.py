# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GaokaoItem(scrapy.Item):
    # define the fields for your item here like:
    school_name = scrapy.Field()
    # 学校ID
    school_id = scrapy.Field()
    # 省份ID
    province_id = scrapy.Field()
