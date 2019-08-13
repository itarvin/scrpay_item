# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
from scrapy.utils.project import get_project_settings
settings = get_project_settings()
class FengniaoPipeline(object):
    def process_item(self, item, spider):
        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c=settings['CHARSET']
        port=settings['MYSQL_PORT']
        title = json.dumps(item['title'], ensure_ascii = False)
        category = json.dumps(item['category'], ensure_ascii = False)
        addtime = json.dumps(item['addtime'], ensure_ascii = False)
        contents = json.dumps(item['content'], ensure_ascii = False)
        content1 = ''
        content2 = contents.strip()
        content  = content1.join(content2)
        #数据库连接
        con=pymysql.connect(host=host,user=user,passwd=psd,db=db,charset=c,port=port)
        #数据库游标
        cue=con.cursor()
        print("mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
        try:
            cue.execute("insert into picture (title,addtime,category,content,url) values(%s,%s,%s,%s,%s)",[ title.replace('"', ''),addtime.replace('"', ''),category.replace('"', ''),content.replace('"', ''),item['url'].replace('"', '')])
            print("insert success")#测试语句
        except Exception as e:
            print('Insert error:',e)
            con.rollback()
        else:
            con.commit()
        con.close()
        return item
