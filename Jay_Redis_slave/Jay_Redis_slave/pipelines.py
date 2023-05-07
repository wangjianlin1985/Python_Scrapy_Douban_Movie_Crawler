# -*- coding: utf-8 -*-
#from pymongo import MongoClient
from scrapy import logformatter
import traceback
from scrapy.exceptions import DropItem


import MySQLdb

class MongodbPipeline(object):
    #MONGODB_SERVER = '122.51.95.201'
    #MONGODB_PORT = 27017
    #MONGODB_DB = 'JayMongo'
    #MONGODB_USER = 'root'
    #MONGODB_PWD = '919169807'

    MYSQL_SERVER = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_DB = 'movie_db'
    MYSQL_USER = 'root'
    MYSQL_PWD = '123456'

    def __init__(self):
        try:
            #self.client = MongoClient(host=self.MONGODB_SERVER, port=self.MONGODB_PORT)
            #self.db = self.client[self.MONGODB_DB]
            #self.db.authenticate(name=self.MONGODB_USER, password=self.MONGODB_PWD)
            #self.col = self.db["movie_content"]

            # 打开数据库连接
            self.db = MySQLdb.connect(self.MYSQL_SERVER, self.MYSQL_USER, self.MYSQL_PWD, self.MYSQL_DB, charset='utf8')
            # 使用cursor()方法获取操作游标
            self.cursor = self.db.cursor()



        except Exception:
            traceback.print_exc()

    @classmethod
    def from_crawler(cls, crawler):
        #cls.MONGODB_SERVER = crawler.settings.get('SingleMONGODB_SERVER', '122.51.95.201')
        #cls.MONGODB_PORT = crawler.settings.getint('SingleMONGODB_PORT', 27017)
        #cls.MONGODB_DB = crawler.settings.get('SingleMONGODB_DB', 'JayMongo')
        #cls.MONGODB_USER = crawler.settings.get('SingleMONGODB_USER', 'root')
        #cls.MONGODB_PWD = crawler.settings.get('SingleMONGODB_PWD', '919169807')

        pipe = cls()
        pipe.crawler = crawler
        return pipe

    def process_item(self, item, spider):
        # if item['a'] == 0:
        #     raise DropItem("Duplicate item found: %s" % item)
        movie_detail = {
            'url': item.get('url'),
            'title': item.get('title'),
            'director': item.get('director'),
            'screenwriter': item.get('screenwriter'),
            'actors': item.get('actors'),
            'category': item.get('category'),
            'country': item.get('country'),
            'langrage': item.get('langrage'),
            'initial': item.get('initial'),
            'runtime': item.get('runtime'),
            'playUrl': item.get('playUrl'),
            'rate': item.get('rate'),
            'starPeople': item.get('starPeople'),
            'preShowUrl': item.get('preShowUrl'),
            'intro': item.get('intro'),
            'icon': item.get('icon')
        }

        delte_sql = "DELETE FROM t_movie WHERE url='%s'" % movie_detail['url']
        # SQL 插入语句
        insert_sql = "INSERT INTO t_movie(url,title,director,screenwriter,actors,category,country,langrage,initial,runtime,playUrl,rate,starPeople,preShowUrl,intro,icon) \
                  VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (movie_detail['url'],movie_detail['title'],movie_detail['director'],movie_detail['screenwriter'],movie_detail['actors'],  \
               movie_detail['category'],movie_detail['country'],movie_detail['langrage'],movie_detail['initial'],movie_detail['runtime'], \
               movie_detail['playUrl'],movie_detail['rate'],movie_detail['starPeople'],movie_detail['preShowUrl'],movie_detail['intro'], \
               movie_detail['icon'])

        try:
            # 执行sql语句
            self.cursor.execute(delte_sql)
            self.cursor.execute(insert_sql)
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            print('插入数据库发生错误：%s' % e)
            # 发生错误时回滚
            self.db.rollback()

        # 关闭数据库连接
        #self.db.close()

        #result = self.col.insert(movie_detail)
        print('[success] insert ' + item['url'] + ' title:' + item['title'])
        return item

