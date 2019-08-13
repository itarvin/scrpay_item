# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from model.items import ModelItem


class MeinvSpider(CrawlSpider):
    name = 'meinv'
    allowed_domains = ['www.2717.com']
    start_urls = ['http://www.2717.com/ent/%s/' % i for i in ['mingxingtuku', 'meinvtupian', 'rentiyishu']]
    pagelink = LinkExtractor(allow=r'list_\d+_\d+.html')
    contentlink = LinkExtractor(allow=r'/ent/\w+/\d+/\d+.html')
    rules = (
        Rule(pagelink),
        Rule(contentlink, callback = 'parse_item'),
    )
    def parse_item(self, response):
        item = ModelItem()
        item['content'] = response.xpath('//*[@id="picBody"]/p/a[1]/img/@src').extract()[-1]
        item['title'] = response.xpath('/html/head/title/text()').extract()[-1].split('-')[0]
        item['url'] = response.url
        yield item
