import random
import requests

proxies = [
    #{'http':'socks5://182.138.238.63:9999'},
    #{'https':'socks5://171.11.179.112:9999'}
    {'http':'socks5://171.35.148.172:9999'},
]
proxies = random.choice(proxies)
print(proxies)
url = 'http://icanhazip.com'
try:
    response = requests.get(url,proxies=proxies) #使用代理
    print(response.status_code)
    if response.status_code == 200:
        print(response.text)
except requests.ConnectionError as e:
    print(e.args)