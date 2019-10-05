# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy.utils.project import get_project_settings
settings = get_project_settings()
import random
import time
# User-Agetn 下载中间件
class RandomUserAgent(object):
    def process_request(self, request, spider):
        # print(settings['USER_AGENTS'])
        # 这句话用于随机选择user-agent
        user_agent = random.choice(settings['USER_AGENTS'])
        date = time.strftime(u"%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
        #print user_agent
        request.headers.setdefault('User-Agent', user_agent)
        #request.headers.setdefault('If-Modified-Since', date)
