from 配置文件 import redis_link

BOT_NAME = 'BiShe'
SPIDER_MODULES = ['BiShe.spiders']
NEWSPIDER_MODULE = 'BiShe.spiders'
ROBOTSTXT_OBEY = False
# LOG_LEVEL = 'INFO'
LOG_LEVEL = 'ERROR'

COOKIES_ENABLED = True
#CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 1

# 并发请求数
CONCURRENT_REQUESTS_PER_DOMAIN = 4

# 单个IP地址发出的并发请求最大数量
CONCURRENT_REQUESTS_PER_IP = 4


DOWNLOADER_MIDDLEWARES = {
   'BiShe.middlewares.BisheDownloaderMiddleware': 543,
}

ITEM_PIPELINES = {
   'BiShe.pipelines.TouPipeline': 300,
   'BiShe.pipelines.WeiPipeline': 301,
}

# 数据库配置, redis调度器
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# DUPEFILTER_CLASS = 'BiShe.MyDupeFilter.MyDupeFilter1'
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# DUPEFILTER_CLASS = None

# Redis服务器地址
REDIS_HOST = redis_link[0]['host']

# Redis服务器端口
REDIS_PORT = redis_link[0]['port']
REDIS_PARAMS = {
    'password': redis_link[0]['password'],
    'db': 0,
    # 'decode_responses': True,
}
