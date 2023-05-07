# -*- coding: utf-8 -*-
# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
import random
from Jay_Redis.utils.GetProxyIp import GetIps


class Proxy_Middleware:
    global count
    count = 1
    global ips
    ips = []

    def process_request(self, request, spider):
        global count
        global ips
        if count == 1:
            ips = GetIps()
        elif count % 100 == 0:
            ips = []
            ips = GetIps()
        else:
            pass
        try:
            num = random.randint(0, len(ips))
            ress = 'http://' + ips[num]
        except Exception as e:
            print(e)
        else:
            request.meta['proxy'] = str(ress)
            count += 1
