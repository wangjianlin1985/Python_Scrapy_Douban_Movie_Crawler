# -*- coding: utf-8 -*-
BOT_NAME = 'Jay_Redis_slave'

SPIDER_MODULES = ['Jay_Redis_slave.spiders']
NEWSPIDER_MODULE = 'Jay_Redis_slave.spiders'

""" scrapy-redis配置 """

USER_AGENT = "Jay's_Redis(+q1055358033If something goes wrong/DoingMyGraduationProject~/FullFunctionTest^……^)"

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 16

# DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

COOKIES_ENABLED = False

TELNETCONSOLE_ENABLED = False

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = False
# 是否在项目停止后保留调度器和去重记录
# 自己做去重,不需要自带的dupefilter

REDIS_HOST = "127.0.0.1"
REDIS_PORT = "6379"
REDIS_PARAMS ={
    'password': '',  # 服务器的redis对应密码
}

# 去除scrapy里面的debug消息的
LOG_LEVEL = 'INFO'
LOG_ENABLED = False

#SingleMONGODB_SERVER = "122.51.95.201"
#SingleMONGODB_PORT = 27017
#SingleMONGODB_DB = "JayMongo"
#SingleMONGODB_USER = 'root'
#SingleMONGODB_PWD = '919169807'

ITEM_PIPELINES = {
   'Jay_Redis_slave.pipelines.MongodbPipeline': 300,
}


# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Jay_Redis_slave.middlewares.JayRedisSlaveSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Jay_Redis_slave.middlewares.JayRedisSlaveDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'





