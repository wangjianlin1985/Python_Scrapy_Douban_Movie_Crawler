# -*- coding: utf-8 -*-
# Author : Jay
# writeTime : 2019/11/16 intern ing!

import redis


def insert_into_start_urls():
    # 为redis插入start_urls
    try:
        r = redis.Redis(host='127.0.0.1', port='6379', db=0, password='')
    except Exception as e:
        print('连接redis失败, %s' % e)
    else:
        try:

            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_'
                                  'limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8F%AF%E6%92%AD%E6%94'
                                  '%BE&sort=time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB'
                                  '%98%E5%88%86&sort=time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%86%B7%E9%97%A8%E4%BD'
                                  '%B3%E7%89%87&sort=time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8D%8E%E8%AF%AD&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%AC%A7%E7%BE%8E&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E9%9F%A9%E5%9B%BD&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%97%A5%E6%9C%AC&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8A%A8%E4%BD%9C&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%96%9C%E5%89%A7&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%88%B1%E6%83%85&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%A7%91%E5%B9%BB&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%82%AC%E7%96%91&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%81%90%E6%80%96&sort='
                                  'time&page_limit=100&page_start=0')
            r.lpush('start_urls', 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%88%90%E9%95%BF&sort='
                                  'time&page_limit=100&page_start=0')
            # 分类界面的 20一跳
            r.lpush('start_urls', 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5'
                                  '%BD%B1&start=20')
            r.close()
            print('push into start_urls queue Done!')
        except Exception as e:
            print('插入redis失败, %s' % e)


def insert_new_start_urls(url):
    # 为redis插入新的urls
    try:
        r = redis.Redis(host='127.0.0.1', port='6379', db=0, password='')
    except Exception as e:
        print('连接redis失败, %s' % e)
    else:
        try:
            r.lpush('start_urls', url)
            #r.sadd('start_urls', url)
            r.close()
        except Exception as e:
            print(e)


def insert_content_urls(url):
    # 为redis插入content urls
    try:
        r = redis.Redis(host='127.0.0.1', port='6379', db=0, password='')
    except Exception as e:
        print('连接redis失败, %s' % e)
    else:
        try:
            r.lpush('content_urls', url)
            #r.sadd('content_urls', url)
            r.close()
        except Exception as e:
            print(e)
