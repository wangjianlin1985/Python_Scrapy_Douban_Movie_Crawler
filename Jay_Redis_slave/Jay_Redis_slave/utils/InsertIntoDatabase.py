# -*- coding: utf-8 -*-
# Author : Jay
# writeTime : 2019/11/18 intern ing!

import redis


def no_dup_request(url):
    # 将这个作为去重方法，每次读一个url就存入此处，爬之前查重，如果存在就不爬
    try:
        r = redis.Redis(host='127.0.0.1', port='6379', db=0, password='')
    except Exception as e:
        print('连接redis失败, %s' % e)
    else:
        try:
            a = r.sadd('NoDupUrls', url)
            r.close()
            if a == 1:
                return True
            else:
                return False
        except Exception as e:
            print('insert NoDupUrls error %s' % e)
