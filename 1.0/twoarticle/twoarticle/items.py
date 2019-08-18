# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TwoarticleItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    cate = scrapy.Field()
    addtime = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
