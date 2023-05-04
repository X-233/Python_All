from 配置文件1 import redis_link
BOT_NAME = "gaokao"

SPIDER_MODULES = ["gaokao.spiders"]
NEWSPIDER_MODULE = "gaokao.spiders"
LOG_LEVEL = "ERROR"
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 4
RETRY_TIMES = 5
DOWNLOAD_DELAY = 4
DOWNLOADER_MIDDLEWARES = {
   "gaokao.middlewares.GaokaoDownloaderMiddleware": 543,
}

ITEM_PIPELINES = {
   "gaokao.pipelines.GaokaoPipeline": 300,
}

FEED_EXPORT_ENCODING = "utf-8"


SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# Redis服务器地址
REDIS_HOST = redis_link[1]['host']

# Redis服务器端口
REDIS_PORT = redis_link[1]['port']

REDIS_PARAMS = {
    'password': redis_link[1]['password'],
    'db': 0,
    # 'decode_responses': True,
}