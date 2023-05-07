# -*- coding: utf-8 -*-
# Author : Jay
# writeTime : 2019/11/16 intern ing!

from scrapy_redis.spiders import RedisSpider
from Jay_Redis.utils.InsertIntoDatabase import insert_content_urls, insert_new_start_urls, insert_into_start_urls
import json
import re


class MySpider(RedisSpider):
    name = 'MasterDouban'
    allowed_domains = ['movie.douban.com']
    redis_key = 'start_urls'
    insert_into_start_urls()
    print('>>>>>>>>>>')
    print('>>>>>>>>>>>>>>>>>>>>')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>豆瓣master端爬虫启动')
    # if filter in master_end, slave_ends read urls then delete, error pops

    def parse(self, response):
        
        # if self.count > 10:
        #     self.crawler.engine.close_spider('queue is empty, the spider close')
