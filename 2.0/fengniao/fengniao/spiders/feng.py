# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fengniao.items import FengniaoItem

class FengSpider(RedisCrawlSpider):
    name = 'feng'
    
    allowed_domains = ['pp.fengniao.com']

    redis_key = "fengspider:start_urls"

    pagelink = LinkExtractor(allow=r'http://pp.fengniao.com/album_\d+_\d+.html')
    contentlink = LinkExtractor(allow=r'https://pp.fengniao.com/\d+.html')

    rules = (
        Rule(pagelink),
        Rule(contentlink, callback = 'parse_item'),
    )
    def parse_item(self, response):
        item = FengniaoItem()
        prefix = '/html/body/div[4]/div/div'
        item['title'] = response.xpath(prefix + '/h3/text()').extract()[-1]
        item['addtime'] = response.xpath(prefix + '/div[2]/span[7]/text()').extract()[-1]
        item['content'] = response.xpath('//*[@id="contentBox"]/div/div/img/@src').extract()
        item['category'] = response.xpath(prefix +'/div[1]/a[2]/text()').extract()[-1]
        item['url'] = response.url
        yield item
