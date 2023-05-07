# -*- coding: utf-8 -*-
# Author : Jay
# writeTime : 2019/11/18 intern ing!

from scrapy_redis.spiders import RedisSpider


from Jay_Redis_slave.utils.InsertIntoDatabase import no_dup_request
from scrapy.selector import Selector
from Jay_Redis_slave.items import MovieItem
defaultEncoding = 'utf-8'


class MySpider(RedisSpider):


    # 如果设置了DOWNLOAD_DELAY 那么，总的延时应该是两者之和：
    # total_delay = DOWNLOAD_DELAY + RANDOM_DELAY
    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "RANDOM_DELAY": 3,
        "DOWNLOADER_MIDDLEWARES": {
            "Jay_Redis_slave.middlewares.random_delay_middleware.RandomDelayMiddleware": 999,
        }
    }


    name = 'SlaveDouban'
    allowed_domains = ['movie.douban.com']
    redis_key = 'content_urls'
    print('>>>>>>>>>>')
    print('>>>>>>>>>>>>>>>>>>>>')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>豆瓣slave端爬虫启动')

    # TODO 对抓取到的播放url需要进行处理，此处的url不是直连的url，而是带有自身广告的各种接口的url，无法直接破解播放
    def parse(self, response):
        try:
            verify = no_dup_request(response.url)
            
        except Exception as e:
            print('extract error %s, %s' % (e, response.url))



