import redis
import pymysql
import json
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

def process_item():
    # 创建redis数据库连接
    rediscli = redis.Redis(host = "127.0.0.1", password='root', port = 6379, db = 0)

    offset = 0
    error = 0

    while True:
        # 将数据从redis里pop出来
        source, data = rediscli.blpop("xpaha:items")
        item = json.loads(data)
        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c = settings['CHARSET']
        port = settings['MYSQL_PORT']
        # base = json.dumps(item['base'], ensure_ascii = False)
        # develop = json.dumps(item['develop'], ensure_ascii = False)
        # xiangxi = json.dumps(item['xiangxi'], ensure_ascii = False)
        # guhanyu = json.dumps(item['guhanyu'], ensure_ascii = False)

        zi = json.dumps(item['zi'], ensure_ascii = False)
        # #数据库连接
        con=pymysql.connect(host=host,user=user,passwd=psd,db=db,charset=c,port=port)
        #数据库游标
        cue=con.cursor()
        print("mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
        print(zi)
        try:
            if item['zi'] != '':
                cue.execute("insert into zidian (zi,thumb,pinyin,wuxing,jiegou,bushou,bihua,base,kangxi,guhanyu,xiangxi,develop,request) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[ item['zi'],item['thumb'],item['pinyin'],item['wuxing'],item['jiegou'],item['bushou'],item['bihua'],item['base'],item['kangxi'],item['guhanyu'],item['xiangxi'],item['develop'], item['request']])
                print("insert success")#测试语句
            offset += 1
        except Exception as e:
            print('Insert error:',e)
            error += 1
            con.rollback()
        else:
            con.commit()
        print(offset, error)
        con.close()

if __name__ == "__main__":
    process_item()
