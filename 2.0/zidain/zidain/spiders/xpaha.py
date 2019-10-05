# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from zidain.items import ZidainItem

class XpahaSpider(RedisCrawlSpider):
    name = 'xpaha'
    allowed_domains = ['zidian.xpcha.com']
    start_urls = ['http://zidian.xpcha.com/']
    redis_key = "zidianspider:start_urls"

    # pagelink = LinkExtractor(allow=r'href="/hans/\w+')
    contentlink = LinkExtractor(allow=r'\w.html')

    rules = (
        # Rule(pagelink),
        Rule(contentlink, callback = 'parse_item'),
    )

    def parse_item(self, response):
        item = ZidainItem()
        item['zi'] = self.get_zi(response)
        item['thumb'] = self.get_thumb(response)
        item['pinyin'] = self.get_pinyin(response)
        item['wuxing'] = self.get_wuxing(response)
        item['jiegou'] = self.get_jiegou(response)
        item['bushou'] = self.get_bushou(response)
        item['bihua'] = self.get_bihua(response)
        item['base'] = self.get_base(response)
        item['kangxi'] = self.get_kangxi(response)
        item['guhanyu'] = self.get_guhanyu(response)
        item['xiangxi'] = self.get_xiangxi(response)
        item['develop'] = self.get_develop(response)
        item['request'] = response.url
        yield item


    def get_zi(self, response):
        try:
            item = response.xpath('/html/body/div[5]/div[1]/dl/dt[6]/a/text()').extract()[0].split()[-1]
        except Exception as e:
            item = ''

        if len(item):
            item
        return item

    def get_thumb(self, response):
        try:
            item = response.xpath('/html/body/div[5]/div[1]/div[1]/img/@src').extract()[-1]
        except Exception as e:
            item = ''
        if len(item):
            item
        return item

    def get_pinyin(self, response):
        try:
            item = response.css('body > div.body_1000 > div.left_leirong > h1').extract()[-1]
        except Exception as e:
            item = ''

        if len(item):
            item
        return item

    def get_wuxing(self, response):
        try:
            item = response.xpath('/html/body/div[5]/div[1]/div[1]/dl/dd[3]/text()').extract()[-1].split('：')[1]
        except Exception as e:
            item = ''

        if len(item):
            item
        return item

    def get_jiegou(self, response):
        try:
            item = response.xpath('/html/body/div[5]/div[1]/div[1]/dl/dd[5]/text()').extract()[-1].split('：')[1]
        except Exception as e:
            item = ''

        if len(item):
            item
        return item

    def get_bushou(self, response):
        try:
            item = response.xpath('/html/body/div[5]/div[1]/div[1]/dl/dd[1]/text()').extract()[-1].split('：')[1]
        except Exception as e:
            item = ''

        if len(item):
            item
        return item

    def get_bihua(self, response):
        try:
            item = response.xpath('/html/body/div[5]/div[1]/div[1]/dl/dd[2]/text()').extract()[-1].split('：')[1]
        except Exception as e:
            item = ''

        if len(item):
            item
        return item

    def get_base(self, response):
        try:
            item = response.xpath('//*[@id="jbjs"]').extract()[-1]
        except Exception as e:
            item = ''

        if len(item):
            item
        return item

    def get_kangxi(self, response):
        try:
            item = response.css('.zidian_tab a::attr(href)').extract()[2]
        except Exception as e:
            item = ''

        if len(item):
            item
        return item

    def get_guhanyu(self, response):
        try:
            item = response.xpath('//*[@id="ghyzd"]/div').extract()[-1]
        except Exception as e:
            item = ''

        if len(item):
            item
        return item

    def get_xiangxi(self, response):
        try:
            item = response.xpath('//*[@id="xxjs"]/div').extract()[-1]
        except Exception as e:
            item = ''
        if len(item):
            item
        return item

    def get_develop(self, response):
        try:
            item = response.xpath('//*[@id="jbjs"]/dl').extract()[-1]
        except Exception as e:
            item = ''

        if len(item):
            item
        return item
