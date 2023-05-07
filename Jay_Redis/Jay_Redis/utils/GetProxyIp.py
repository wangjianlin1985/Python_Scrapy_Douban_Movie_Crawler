# -*- utf-8 -*-
import random
import redis
import requests

def GetIps():
    li = []
    # url = 'http://122.51.95.201:8000/?country=国内&count=20'
    url = 'http://127.0.0.1:8000/?country=国内&count=20'
    ips = requests.get(url)
    for ip in eval(ips.content):
        li.append(ip[0]+':'+str(ip[1]))
    return li

# GetIps()
