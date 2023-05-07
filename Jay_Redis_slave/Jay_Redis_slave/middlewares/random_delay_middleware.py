import logging
import random
import time


class RandomDelayMiddleware(object):
    def __init__(self, delay):
        self.delay = delay

    @classmethod
    def from_crawler(cls, crawler):
        delay = crawler.spider.settings.get("RANDOM_DELAY", 10)
        if not isinstance(delay, int):
            raise ValueError("RANDOM_DELAY need a int")
        return cls(delay)

    def process_request(self, request, spider):
        #delay = random.randint(0, self.delay)
        delay = random.randint(1, self.delay)
        logging.debug("### random delay: %s s ###" % delay)
        time.sleep(delay)
        #request.meta['proxy'] = ip