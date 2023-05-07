#!/usr/bin/python
# -*-coding:utf-8-*-

from fake_useragent import UserAgent


class RotateUserAgentMiddleware(object):
    """
       a useragent middleware which rotate the user agent when crawl websites

       if you set the USER_AGENT_LIST in settings,the rotate with it,if not,then use the default user_agent_list
       attribute instead.
    """

    def __init__(self, crawler, ):
        super(RotateUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        request.headers.setdefault("User-Agent", self.ua.random)
