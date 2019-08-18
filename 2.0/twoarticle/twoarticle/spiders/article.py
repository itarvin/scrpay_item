# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from twoarticle.items import TwoarticleItem

class ArticleSpider(RedisCrawlSpider):
    name = 'article'

    allowed_domains = ['www.027it.cn']

    redis_key = "articlespider:start_urls"
    # start_urls = ['http://www.027it.cn/list-%d-0.html' % i for i in range(1,216)]
    pagelink = LinkExtractor(allow=r'http://www.027it.cn/list-\d+-\d+.html')
    contentlink = LinkExtractor(allow=r'http://www.027it.cn/article-\d+-\d+-\d+.html')
    rules = (
        Rule(contentlink, callback = 'parse_item'),
        Rule(pagelink),
    )

    def parse_item(self, response):
        item = TwoarticleItem()
        item['title'] = response.xpath('//*[@id="title"]/h1/a/text()').extract()[-1]
        # 添加时间
        item['addtime'] = response.xpath('//*[@id="title"]/text()').extract()[-2].split()[1]
        item['cate'] = response.xpath('//*[@id="place"]/a[3]/text()').extract()[-1]
        # 内容
        item['content'] = response.xpath('//*[@id="contents"]').extract()
        # 链接
        item['url'] = response.url
        #
        yield item
