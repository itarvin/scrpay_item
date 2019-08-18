![](https://avatars1.githubusercontent.com/u/32347498?s=460&v=4)

#1.抓取['[二七文章网](<http://www.027it.cn/>)']
```json
1.0 单独执行
```

​	无意间发现该站点的规律，可自行配置数据库，对应字段即可，我本地需要部分文章数据。故爬取了该站点。请勿恶意对该站点的进行恶意请求，爬数据。该站点存在封禁IP的可能，请自行对ip代理处理。挖个坑（2019-08-12）,后续填上。

```json
2.0 分布式
```
​	1.自行配置mysql,redis,mongodb，此处设置了多user-agent,随机应对反爬虫的处理封禁IP的措施！

​	2.可复制一份程序出来，利用anaconda 3配置多个环境，每个环境可以执行一个。加快处理。
​	
​	3.redis执行master执行 : lpush articlespider:start_urls http://www.027it.cn/list-1-0.html http://www.027it.cn/list-2-0.html http://www.027it.cn/list-3-0.html http://www.027it.cn/list-4-0.html http://www.027it.cn/list-5-0.html http://www.027it.cn/list-6-0.html http://www.027it.cn/list-7-0.html http://www.027it.cn/list-8-0.html http://www.027it.cn/list-9-0.html http://www.027it.cn/list-10-0.html http://www.027it.cn/list-11-0.html http://www.027it.cn/list-12-0.html http://www.027it.cn/list-13-0.html http://www.027it.cn/list-14-0.html http://www.027it.cn/list-15-0.html http://www.027it.cn/list-16-0.html http://www.027it.cn/list-17-0.html http://www.027it.cn/list-18-0.html http://www.027it.cn/list-19-0.html http://www.027it.cn/list-20-0.html http://www.027it.cn/list-21-0.html http://www.027it.cn/list-22-0.html http://www.027it.cn/list-23-0.html http://www.027it.cn/list-24-0.html http://www.027it.cn/list-25-0.html http://www.027it.cn/list-26-0.html http://www.027it.cn/list-27-0.html http://www.027it.cn/list-28-0.html http://www.027it.cn/list-29-0.html http://www.027it.cn/list-30-0.html http://www.027it.cn/list-31-0.html http://www.027it.cn/list-32-0.html http://www.027it.cn/list-33-0.html http://www.027it.cn/list-34-0.html http://www.027it.cn/list-35-0.html http://www.027it.cn/list-36-0.html http://www.027it.cn/list-37-0.html http://www.027it.cn/list-38-0.html http://www.027it.cn/list-39-0.html http://www.027it.cn/list-40-0.html http://www.027it.cn/list-41-0.html http://www.027it.cn/list-42-0.html http://www.027it.cn/list-43-0.html http://www.027it.cn/list-44-0.html http://www.027it.cn/list-45-0.html http://www.027it.cn/list-46-0.html http://www.027it.cn/list-47-0.html http://www.027it.cn/list-48-0.html http://www.027it.cn/list-49-0.html http://www.027it.cn/list-50-0.html http://www.027it.cn/list-51-0.html http://www.027it.cn/list-52-0.html http://www.027it.cn/list-53-0.html http://www.027it.cn/list-54-0.html http://www.027it.cn/list-55-0.html http://www.027it.cn/list-56-0.html http://www.027it.cn/list-57-0.html http://www.027it.cn/list-58-0.html http://www.027it.cn/list-59-0.html http://www.027it.cn/list-60-0.html http://www.027it.cn/list-61-0.html http://www.027it.cn/list-62-0.html http://www.027it.cn/list-63-0.html http://www.027it.cn/list-64-0.html http://www.027it.cn/list-65-0.html http://www.027it.cn/list-66-0.html http://www.027it.cn/list-67-0.html http://www.027it.cn/list-68-0.html http://www.027it.cn/list-69-0.html http://www.027it.cn/list-70-0.html http://www.027it.cn/list-71-0.html http://www.027it.cn/list-72-0.html http://www.027it.cn/list-73-0.html http://www.027it.cn/list-74-0.html http://www.027it.cn/list-75-0.html http://www.027it.cn/list-76-0.html http://www.027it.cn/list-77-0.html http://www.027it.cn/list-78-0.html http://www.027it.cn/list-79-0.html http://www.027it.cn/list-80-0.html http://www.027it.cn/list-81-0.html http://www.027it.cn/list-82-0.html http://www.027it.cn/list-83-0.html http://www.027it.cn/list-84-0.html http://www.027it.cn/list-85-0.html http://www.027it.cn/list-86-0.html http://www.027it.cn/list-87-0.html http://www.027it.cn/list-88-0.html http://www.027it.cn/list-89-0.html http://www.027it.cn/list-90-0.html http://www.027it.cn/list-91-0.html http://www.027it.cn/list-92-0.html http://www.027it.cn/list-93-0.html http://www.027it.cn/list-94-0.html http://www.027it.cn/list-95-0.html http://www.027it.cn/list-96-0.html http://www.027it.cn/list-97-0.html http://www.027it.cn/list-98-0.html http://www.027it.cn/list-99-0.html http://www.027it.cn/list-100-0.html http://www.027it.cn/list-101-0.html http://www.027it.cn/list-102-0.html http://www.027it.cn/list-103-0.html http://www.027it.cn/list-104-0.html http://www.027it.cn/list-105-0.html http://www.027it.cn/list-106-0.html http://www.027it.cn/list-107-0.html http://www.027it.cn/list-108-0.html http://www.027it.cn/list-109-0.html http://www.027it.cn/list-110-0.html http://www.027it.cn/list-111-0.html http://www.027it.cn/list-112-0.html http://www.027it.cn/list-113-0.html http://www.027it.cn/list-114-0.html http://www.027it.cn/list-115-0.html

​		lpush articlespider:start_urls http://www.027it.cn/list-116-0.html http://www.027it.cn/list-117-0.html http://www.027it.cn/list-118-0.html http://www.027it.cn/list-119-0.html http://www.027it.cn/list-120-0.html http://www.027it.cn/list-121-0.html http://www.027it.cn/list-122-0.html http://www.027it.cn/list-123-0.html http://www.027it.cn/list-124-0.html http://www.027it.cn/list-125-0.html http://www.027it.cn/list-126-0.html http://www.027it.cn/list-127-0.html http://www.027it.cn/list-128-0.html http://www.027it.cn/list-129-0.html http://www.027it.cn/list-130-0.html http://www.027it.cn/list-131-0.html http://www.027it.cn/list-132-0.html http://www.027it.cn/list-133-0.html http://www.027it.cn/list-134-0.html http://www.027it.cn/list-135-0.html http://www.027it.cn/list-136-0.html http://www.027it.cn/list-137-0.html http://www.027it.cn/list-138-0.html http://www.027it.cn/list-139-0.html http://www.027it.cn/list-140-0.html http://www.027it.cn/list-141-0.html http://www.027it.cn/list-142-0.html http://www.027it.cn/list-143-0.html http://www.027it.cn/list-144-0.html http://www.027it.cn/list-145-0.html http://www.027it.cn/list-146-0.html http://www.027it.cn/list-147-0.html http://www.027it.cn/list-148-0.html http://www.027it.cn/list-149-0.html http://www.027it.cn/list-150-0.html http://www.027it.cn/list-151-0.html http://www.027it.cn/list-152-0.html http://www.027it.cn/list-153-0.html http://www.027it.cn/list-154-0.html http://www.027it.cn/list-155-0.html http://www.027it.cn/list-156-0.html http://www.027it.cn/list-157-0.html http://www.027it.cn/list-158-0.html http://www.027it.cn/list-159-0.html http://www.027it.cn/list-160-0.html http://www.027it.cn/list-161-0.html http://www.027it.cn/list-162-0.html http://www.027it.cn/list-163-0.html http://www.027it.cn/list-164-0.html http://www.027it.cn/list-165-0.html http://www.027it.cn/list-166-0.html http://www.027it.cn/list-167-0.html http://www.027it.cn/list-168-0.html http://www.027it.cn/list-169-0.html http://www.027it.cn/list-170-0.html http://www.027it.cn/list-171-0.html http://www.027it.cn/list-172-0.html http://www.027it.cn/list-173-0.html http://www.027it.cn/list-174-0.html http://www.027it.cn/list-175-0.html http://www.027it.cn/list-176-0.html http://www.027it.cn/list-177-0.html http://www.027it.cn/list-178-0.html http://www.027it.cn/list-179-0.html http://www.027it.cn/list-180-0.html http://www.027it.cn/list-181-0.html http://www.027it.cn/list-182-0.html http://www.027it.cn/list-183-0.html http://www.027it.cn/list-184-0.html http://www.027it.cn/list-185-0.html http://www.027it.cn/list-186-0.html http://www.027it.cn/list-187-0.html http://www.027it.cn/list-188-0.html http://www.027it.cn/list-189-0.html http://www.027it.cn/list-190-0.html http://www.027it.cn/list-191-0.html http://www.027it.cn/list-192-0.html http://www.027it.cn/list-193-0.html http://www.027it.cn/list-194-0.html http://www.027it.cn/list-195-0.html http://www.027it.cn/list-196-0.html http://www.027it.cn/list-197-0.html http://www.027it.cn/list-198-0.html http://www.027it.cn/list-199-0.html http://www.027it.cn/list-200-0.html http://www.027it.cn/list-201-0.html http://www.027it.cn/list-202-0.html http://www.027it.cn/list-203-0.html http://www.027it.cn/list-204-0.html http://www.027it.cn/list-205-0.html http://www.027it.cn/list-206-0.html http://www.027it.cn/list-207-0.html http://www.027it.cn/list-208-0.html http://www.027it.cn/list-209-0.html http://www.027it.cn/list-210-0.html http://www.027it.cn/list-211-0.html http://www.027it.cn/list-212-0.html http://www.027it.cn/list-213-0.html http://www.027it.cn/list-214-0.html http://www.027it.cn/list-215-0.html http://www.027it.cn/list-216-0.html http://www.027it.cn/list-217-0.html 

   4. 程序端执行: scrapy runspider article.py
         	提取执mysql数据库 : 	      执行 python process_item_item_mysql.py

         ​	提取执mongodb数据库 : 	执行 python process_item_item_mongodb.py



#2.抓取['[蜂鸟网](https://pp.fengniao.com/album_1.html)']

```json
1.0 单独执行
```
前几次对蜂鸟网爬取了图片，真心觉得它的图片不是一般的多，最初爬取了一个分类。下载了近百个G的数据。为此，中断了进程。此次，主要想对它的图片库的全面进行清洗。把图片链接的地址打包存进数据库。便于后续下载后调用。此网站的没有做任何防范爬取的措施，提取很顺畅，它的图放在第三方的图床。
​	注：注意看链接页的链接协议。


```json
2.0 分布式
```
​	1.自行配置mysql,redis,mongodb

​	2.可复制一份程序出来，利用anaconda 3配置多个环境，每个环境可以执行一个。加快处理。

​	redis执行master执行 : lpush fengspider:start_urls https://pp.fengniao.com/album_1.html https://pp.fengniao.com/album_2.html https://pp.fengniao.com/album_3.html https://pp.fengniao.com/album_4.html https://pp.fengniao.com/album_5.html https://pp.fengniao.com/album_6.html https://pp.fengniao.com/album_7.html https://pp.fengniao.com/album_8.html https://pp.fengniao.com/album_9.html https://pp.fengniao.com/album_10.html https://pp.fengniao.com/album_11.html https://pp.fengniao.com/album_12.html https://pp.fengniao.com/album_13.html https://pp.fengniao.com/album_14.html https://pp.fengniao.com/album_15.html https://pp.fengniao.com/album_16.html https://pp.fengniao.com/album_17.html https://pp.fengniao.com/album_18.html https://pp.fengniao.com/album_19.html https://pp.fengniao.com/album_20.html https://pp.fengniao.com/album_21.html https://pp.fengniao.com/album_22.html https://pp.fengniao.com/album_23.html https://pp.fengniao.com/album_24.html https://pp.fengniao.com/album_25.html https://pp.fengniao.com/album_26.html https://pp.fengniao.com/album_27.html https://pp.fengniao.com/album_28.html https://pp.fengniao.com/album_29.html https://pp.fengniao.com/album_30.html https://pp.fengniao.com/album_31.html https://pp.fengniao.com/album_32.html https://pp.fengniao.com/album_33.html https://pp.fengniao.com/album_34.html https://pp.fengniao.com/album_35.html https://pp.fengniao.com/album_36.html https://pp.fengniao.com/album_37.html

   程序端执行: scrapy runspider feng.py
   提取执mysql数据库 : 	      执行 python process_item_item_mysql.py
   提取执mongodb数据库 : 	执行 python process_item_item_mongodb.py




#3.抓取['[2717网](https://www.2717.com/ent/mingxingtuku/)']  ---原27270.com

​	这个网站也是之前爬取过的，中午花了点时间重新对它清洗了一次，几分钟就爬完了，抓了1万4千多条数据（感兴趣的）。此站点有意思的是，里面还有子页图，时间原因，暂处理之间链接进去的，之前用的拼链接。后面再把完整的处理了，又挖个坑（2019-08-13）。









> 声明：此类项目仅供个人学习。
>
> ​	不要对压力测试太过迷恋，除非对方抢了你的糖果！                    -----------------《黑客守则》
