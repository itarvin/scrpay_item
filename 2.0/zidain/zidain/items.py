# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZidainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zi =  scrapy.Field() # response.xpath('/html/body/div[5]/div[1]/dl/dt[6]/a/text()').extract()[0].split()[-1]
    thumb =  scrapy.Field() #response.xpath('/html/body/div[5]/div[1]/div[1]/img/@src').extract()[-1] response.css('.zidian_shuxing img::attr(src)').extract()[-1]
    pinyin =  scrapy.Field() #response.css('body > div.body_1000 > div.left_leirong > h1').extract()[-1]
    wuxing =  scrapy.Field() #response.xpath('/html/body/div[5]/div[1]/div[1]/dl/dd[3]/text()').extract()[-1].split('：')[1]
    jiegou =  scrapy.Field() #response.xpath('/html/body/div[5]/div[1]/div[1]/dl/dd[5]/text()').extract()[-1].split('：')[1]
    bushou =  scrapy.Field()  # response.xpath('/html/body/div[5]/div[1]/div[1]/dl/dd[1]/text()').extract()[-1].split('：')[1]
    bihua =  scrapy.Field()  # response.xpath('/html/body/div[5]/div[1]/div[1]/dl/dd[2]/text()').extract()[-1].split('：')[1]
    base =  scrapy.Field() #response.xpath('//*[@id="jbjs"]').extract()[-1]
    kangxi =  scrapy.Field() # response.css('.zidian_tab a::attr(href)').extract()[2]
    guhanyu =  scrapy.Field() #response.xpath('//*[@id="ghyzd"]/div').extract()[-1]
    xiangxi =  scrapy.Field() # response.xpath('//*[@id="xxjs"]/div').extract()[-1]
    develop =  scrapy.Field() #response.xpath('//*[@id="jbjs"]/dl').extract()[-1]
    request =  scrapy.Field() #response.xpath('//*[@id="jbjs"]/dl').extract()[-1]
