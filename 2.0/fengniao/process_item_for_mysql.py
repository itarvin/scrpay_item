import redis
import pymysql
import json
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

def process_item():
    # 创建redis数据库连接
    rediscli = redis.Redis(host = "127.0.0.1", password='123456', port = 6379, db = 0)

    offset = 0
    error = 0

    while True:
        # 将数据从redis里pop出来
        source, data = rediscli.blpop("feng:items")
        item = json.loads(data)
        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c = settings['CHARSET']
        port = settings['MYSQL_PORT']

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
