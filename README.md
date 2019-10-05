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
​	3.redis执行master执行 :

```json
 lpush articlespider:start_urls http://www.027it.cn/list-1-0.html http://www.027it.cn/list-2-0.html http://www.027it.cn/list-3-0.html http://www.027it.cn/list-4-0.html http://www.027it.cn/list-5-0.html http://www.027it.cn/list-6-0.html http://www.027it.cn/list-7-0.html http://www.027it.cn/list-8-0.html http://www.027it.cn/list-9-0.html http://www.027it.cn/list-10-0.html http://www.027it.cn/list-11-0.html http://www.027it.cn/list-12-0.html http://www.027it.cn/list-13-0.html http://www.027it.cn/list-14-0.html http://www.027it.cn/list-15-0.html http://www.027it.cn/list-16-0.html http://www.027it.cn/list-17-0.html http://www.027it.cn/list-18-0.html http://www.027it.cn/list-19-0.html http://www.027it.cn/list-20-0.html http://www.027it.cn/list-21-0.html http://www.027it.cn/list-22-0.html http://www.027it.cn/list-23-0.html http://www.027it.cn/list-24-0.html http://www.027it.cn/list-25-0.html http://www.027it.cn/list-26-0.html http://www.027it.cn/list-27-0.html http://www.027it.cn/list-28-0.html http://www.027it.cn/list-29-0.html http://www.027it.cn/list-30-0.html http://www.027it.cn/list-31-0.html http://www.027it.cn/list-32-0.html http://www.027it.cn/list-33-0.html http://www.027it.cn/list-34-0.html http://www.027it.cn/list-35-0.html http://www.027it.cn/list-36-0.html http://www.027it.cn/list-37-0.html http://www.027it.cn/list-38-0.html http://www.027it.cn/list-39-0.html http://www.027it.cn/list-40-0.html http://www.027it.cn/list-41-0.html http://www.027it.cn/list-42-0.html http://www.027it.cn/list-43-0.html http://www.027it.cn/list-44-0.html http://www.027it.cn/list-45-0.html http://www.027it.cn/list-46-0.html http://www.027it.cn/list-47-0.html http://www.027it.cn/list-48-0.html http://www.027it.cn/list-49-0.html http://www.027it.cn/list-50-0.html http://www.027it.cn/list-51-0.html http://www.027it.cn/list-52-0.html http://www.027it.cn/list-53-0.html http://www.027it.cn/list-54-0.html http://www.027it.cn/list-55-0.html http://www.027it.cn/list-56-0.html http://www.027it.cn/list-57-0.html http://www.027it.cn/list-58-0.html http://www.027it.cn/list-59-0.html http://www.027it.cn/list-60-0.html http://www.027it.cn/list-61-0.html http://www.027it.cn/list-62-0.html http://www.027it.cn/list-63-0.html http://www.027it.cn/list-64-0.html http://www.027it.cn/list-65-0.html http://www.027it.cn/list-66-0.html http://www.027it.cn/list-67-0.html http://www.027it.cn/list-68-0.html http://www.027it.cn/list-69-0.html http://www.027it.cn/list-70-0.html http://www.027it.cn/list-71-0.html http://www.027it.cn/list-72-0.html http://www.027it.cn/list-73-0.html http://www.027it.cn/list-74-0.html http://www.027it.cn/list-75-0.html http://www.027it.cn/list-76-0.html http://www.027it.cn/list-77-0.html http://www.027it.cn/list-78-0.html http://www.027it.cn/list-79-0.html http://www.027it.cn/list-80-0.html http://www.027it.cn/list-81-0.html http://www.027it.cn/list-82-0.html http://www.027it.cn/list-83-0.html http://www.027it.cn/list-84-0.html http://www.027it.cn/list-85-0.html http://www.027it.cn/list-86-0.html http://www.027it.cn/list-87-0.html http://www.027it.cn/list-88-0.html http://www.027it.cn/list-89-0.html http://www.027it.cn/list-90-0.html http://www.027it.cn/list-91-0.html http://www.027it.cn/list-92-0.html http://www.027it.cn/list-93-0.html http://www.027it.cn/list-94-0.html http://www.027it.cn/list-95-0.html http://www.027it.cn/list-96-0.html http://www.027it.cn/list-97-0.html http://www.027it.cn/list-98-0.html http://www.027it.cn/list-99-0.html http://www.027it.cn/list-100-0.html http://www.027it.cn/list-101-0.html http://www.027it.cn/list-102-0.html http://www.027it.cn/list-103-0.html http://www.027it.cn/list-104-0.html http://www.027it.cn/list-105-0.html http://www.027it.cn/list-106-0.html http://www.027it.cn/list-107-0.html http://www.027it.cn/list-108-0.html http://www.027it.cn/list-109-0.html http://www.027it.cn/list-110-0.html http://www.027it.cn/list-111-0.html http://www.027it.cn/list-112-0.html http://www.027it.cn/list-113-0.html http://www.027it.cn/list-114-0.html http://www.027it.cn/list-115-0.html

​		lpush articlespider:start_urls http://www.027it.cn/list-116-0.html http://www.027it.cn/list-117-0.html http://www.027it.cn/list-118-0.html http://www.027it.cn/list-119-0.html http://www.027it.cn/list-120-0.html http://www.027it.cn/list-121-0.html http://www.027it.cn/list-122-0.html http://www.027it.cn/list-123-0.html http://www.027it.cn/list-124-0.html http://www.027it.cn/list-125-0.html http://www.027it.cn/list-126-0.html http://www.027it.cn/list-127-0.html http://www.027it.cn/list-128-0.html http://www.027it.cn/list-129-0.html http://www.027it.cn/list-130-0.html http://www.027it.cn/list-131-0.html http://www.027it.cn/list-132-0.html http://www.027it.cn/list-133-0.html http://www.027it.cn/list-134-0.html http://www.027it.cn/list-135-0.html http://www.027it.cn/list-136-0.html http://www.027it.cn/list-137-0.html http://www.027it.cn/list-138-0.html http://www.027it.cn/list-139-0.html http://www.027it.cn/list-140-0.html http://www.027it.cn/list-141-0.html http://www.027it.cn/list-142-0.html http://www.027it.cn/list-143-0.html http://www.027it.cn/list-144-0.html http://www.027it.cn/list-145-0.html http://www.027it.cn/list-146-0.html http://www.027it.cn/list-147-0.html http://www.027it.cn/list-148-0.html http://www.027it.cn/list-149-0.html http://www.027it.cn/list-150-0.html http://www.027it.cn/list-151-0.html http://www.027it.cn/list-152-0.html http://www.027it.cn/list-153-0.html http://www.027it.cn/list-154-0.html http://www.027it.cn/list-155-0.html http://www.027it.cn/list-156-0.html http://www.027it.cn/list-157-0.html http://www.027it.cn/list-158-0.html http://www.027it.cn/list-159-0.html http://www.027it.cn/list-160-0.html http://www.027it.cn/list-161-0.html http://www.027it.cn/list-162-0.html http://www.027it.cn/list-163-0.html http://www.027it.cn/list-164-0.html http://www.027it.cn/list-165-0.html http://www.027it.cn/list-166-0.html http://www.027it.cn/list-167-0.html http://www.027it.cn/list-168-0.html http://www.027it.cn/list-169-0.html http://www.027it.cn/list-170-0.html http://www.027it.cn/list-171-0.html http://www.027it.cn/list-172-0.html http://www.027it.cn/list-173-0.html http://www.027it.cn/list-174-0.html http://www.027it.cn/list-175-0.html http://www.027it.cn/list-176-0.html http://www.027it.cn/list-177-0.html http://www.027it.cn/list-178-0.html http://www.027it.cn/list-179-0.html http://www.027it.cn/list-180-0.html http://www.027it.cn/list-181-0.html http://www.027it.cn/list-182-0.html http://www.027it.cn/list-183-0.html http://www.027it.cn/list-184-0.html http://www.027it.cn/list-185-0.html http://www.027it.cn/list-186-0.html http://www.027it.cn/list-187-0.html http://www.027it.cn/list-188-0.html http://www.027it.cn/list-189-0.html http://www.027it.cn/list-190-0.html http://www.027it.cn/list-191-0.html http://www.027it.cn/list-192-0.html http://www.027it.cn/list-193-0.html http://www.027it.cn/list-194-0.html http://www.027it.cn/list-195-0.html http://www.027it.cn/list-196-0.html http://www.027it.cn/list-197-0.html http://www.027it.cn/list-198-0.html http://www.027it.cn/list-199-0.html http://www.027it.cn/list-200-0.html http://www.027it.cn/list-201-0.html http://www.027it.cn/list-202-0.html http://www.027it.cn/list-203-0.html http://www.027it.cn/list-204-0.html http://www.027it.cn/list-205-0.html http://www.027it.cn/list-206-0.html http://www.027it.cn/list-207-0.html http://www.027it.cn/list-208-0.html http://www.027it.cn/list-209-0.html http://www.027it.cn/list-210-0.html http://www.027it.cn/list-211-0.html http://www.027it.cn/list-212-0.html http://www.027it.cn/list-213-0.html http://www.027it.cn/list-214-0.html http://www.027it.cn/list-215-0.html http://www.027it.cn/list-216-0.html http://www.027it.cn/list-217-0.html 
```

   4. 程序端执行: scrapy runspider article.py
         	提取执mysql数据库 : 	      执行

         ```python
         python process_item_item_mysql.py
         ```

         ​	提取执mongodb数据库 : 	执行

         ```python
          python process_item_item_mongodb.py
         ```



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

​	redis执行master执行 :

```json
 	lpush fengspider:start_urls https://pp.fengniao.com/album_1.html https://pp.fengniao.com/album_2.html https://pp.fengniao.com/album_3.html https://pp.fengniao.com/album_4.html https://pp.fengniao.com/album_5.html https://pp.fengniao.com/album_6.html https://pp.fengniao.com/album_7.html https://pp.fengniao.com/album_8.html https://pp.fengniao.com/album_9.html https://pp.fengniao.com/album_10.html https://pp.fengniao.com/album_11.html https://pp.fengniao.com/album_12.html https://pp.fengniao.com/album_13.html https://pp.fengniao.com/album_14.html https://pp.fengniao.com/album_15.html https://pp.fengniao.com/album_16.html https://pp.fengniao.com/album_17.html https://pp.fengniao.com/album_18.html https://pp.fengniao.com/album_19.html https://pp.fengniao.com/album_20.html https://pp.fengniao.com/album_21.html https://pp.fengniao.com/album_22.html https://pp.fengniao.com/album_23.html https://pp.fengniao.com/album_24.html https://pp.fengniao.com/album_25.html https://pp.fengniao.com/album_26.html https://pp.fengniao.com/album_27.html https://pp.fengniao.com/album_28.html https://pp.fengniao.com/album_29.html https://pp.fengniao.com/album_30.html https://pp.fengniao.com/album_31.html https://pp.fengniao.com/album_32.html https://pp.fengniao.com/album_33.html https://pp.fengniao.com/album_34.html https://pp.fengniao.com/album_35.html https://pp.fengniao.com/album_36.html https://pp.fengniao.com/album_37.html
```

   程序端执行: scrapy runspider feng.py
   提取执mysql数据库 : 	      执行 

```python
	python process_item_item_mysql.py
```

   提取执mongodb数据库 : 	执行 

```python
	python process_item_item_mongodb.py
```




#3.抓取['[2717网](https://www.2717.com/ent/mingxingtuku/)']  ---原27270.com

​	这个网站也是之前爬取过的，中午花了点时间重新对它清洗了一次，几分钟就爬完了，抓了1万4千多条数据（感兴趣的）。此站点有意思的是，里面还有子页图，时间原因，暂处理之间链接进去的，之前用的拼链接。后面再把完整的处理了，又挖个坑（2019-08-13）。





#4.抓取['[新华字字典](http://zidian.xpcha.com/)']  ---新华字典

​	抓字典，没说的。13479个字！！

​	根据《新华字典》前言——《新华字典》总共收字11200个左右

至于汉字总共有多少，迄今为止没有准确的数字，这一方面因为汉字太多，难于统计，另一方面因为汉字异体、俗体字太多，这些字能不能统计进汉字的总数，学术界意见不一。

《新华字典》第十一版已于2011年7月出版发行。在最新版本的《新华字典》中，新增了800多个正字头，另外，还增加了1500多个繁体字和500多个异体字。

​	1.自行配置mysql,redis,mongodb

​	2.可复制一份程序出来，利用anaconda 3配置多个环境，每个环境可以执行一个。加快处理。

​	redis执行master执行 : 

​		

```json
lpush zidianspider:start_urls http://zidian.xpcha.com/a.html http://zidian.xpcha.com/ai.html http://zidian.xpcha.com/an.html http://zidian.xpcha.com/ang.html http://zidian.xpcha.com/ao.html http://zidian.xpcha.com/ba.html http://zidian.xpcha.com/bai.html http://zidian.xpcha.com/ban.html http://zidian.xpcha.com/bang.html http://zidian.xpcha.com/bao.html http://zidian.xpcha.com/bei.html http://zidian.xpcha.com/ben.html http://zidian.xpcha.com/beng.html http://zidian.xpcha.com/bi.html http://zidian.xpcha.com/bian.html http://zidian.xpcha.com/biao.html http://zidian.xpcha.com/bie.html http://zidian.xpcha.com/bin.html http://zidian.xpcha.com/bing.html http://zidian.xpcha.com/bo.html http://zidian.xpcha.com/bu.html http://zidian.xpcha.com/ca.html http://zidian.xpcha.com/cai.html http://zidian.xpcha.com/can.html http://zidian.xpcha.com/cang.html http://zidian.xpcha.com/cao.html http://zidian.xpcha.com/ce.html http://zidian.xpcha.com/cen.html http://zidian.xpcha.com/ceng.html http://zidian.xpcha.com/cha.html http://zidian.xpcha.com/chai.html http://zidian.xpcha.com/chan.html http://zidian.xpcha.com/chang.html http://zidian.xpcha.com/chao.html http://zidian.xpcha.com/che.html http://zidian.xpcha.com/chen.html http://zidian.xpcha.com/cheng.html http://zidian.xpcha.com/chi.html http://zidian.xpcha.com/chou.html http://zidian.xpcha.com/chu.html http://zidian.xpcha.com/chua.html http://zidian.xpcha.com/chuai.html http://zidian.xpcha.com/chuan.html http://zidian.xpcha.com/chuang.html http://zidian.xpcha.com/chui.html http://zidian.xpcha.com/chun.html http://zidian.xpcha.com/chuo.html http://zidian.xpcha.com/ci.html http://zidian.xpcha.com/cou.html http://zidian.xpcha.com/cong.html http://zidian.xpcha.com/cu.html http://zidian.xpcha.com/cuan.html http://zidian.xpcha.com/cui.html http://zidian.xpcha.com/cun.html http://zidian.xpcha.com/cuo.html http://zidian.xpcha.com/da.html http://zidian.xpcha.com/dai.html http://zidian.xpcha.com/dan.html http://zidian.xpcha.com/dang.html http://zidian.xpcha.com/dao.html http://zidian.xpcha.com/de.html http://zidian.xpcha.com/den.html http://zidian.xpcha.com/dei.html http://zidian.xpcha.com/deng.html http://zidian.xpcha.com/di.html http://zidian.xpcha.com/dia.html http://zidian.xpcha.com/dian.html http://zidian.xpcha.com/diao.html http://zidian.xpcha.com/die.html http://zidian.xpcha.com/ding.html http://zidian.xpcha.com/diu.html http://zidian.xpcha.com/dong.html http://zidian.xpcha.com/dou.html http://zidian.xpcha.com/du.html http://zidian.xpcha.com/duan.html http://zidian.xpcha.com/dui.html http://zidian.xpcha.com/dun.html http://zidian.xpcha.com/duo.html http://zidian.xpcha.com/e.html http://zidian.xpcha.com/ei.html http://zidian.xpcha.com/en.html http://zidian.xpcha.com/eng.html http://zidian.xpcha.com/er.html http://zidian.xpcha.com/fa.html http://zidian.xpcha.com/fan.html http://zidian.xpcha.com/fang.html http://zidian.xpcha.com/fei.html http://zidian.xpcha.com/fen.html http://zidian.xpcha.com/feng.html http://zidian.xpcha.com/fo.html http://zidian.xpcha.com/fou.html http://zidian.xpcha.com/fu.html http://zidian.xpcha.com/ga.html http://zidian.xpcha.com/gai.html http://zidian.xpcha.com/gan.html http://zidian.xpcha.com/gang.html http://zidian.xpcha.com/gao.html http://zidian.xpcha.com/ge.html http://zidian.xpcha.com/gei.html http://zidian.xpcha.com/gen.html http://zidian.xpcha.com/geng.html http://zidian.xpcha.com/gong.html http://zidian.xpcha.com/gou.html http://zidian.xpcha.com/gu.html http://zidian.xpcha.com/gua.html http://zidian.xpcha.com/guai.html http://zidian.xpcha.com/guan.html http://zidian.xpcha.com/guang.html http://zidian.xpcha.com/gui.html http://zidian.xpcha.com/gun.html http://zidian.xpcha.com/guo.html http://zidian.xpcha.com/ha.html http://zidian.xpcha.com/hai.html http://zidian.xpcha.com/han.html http://zidian.xpcha.com/hang.html http://zidian.xpcha.com/hao.html http://zidian.xpcha.com/he.html http://zidian.xpcha.com/hei.html http://zidian.xpcha.com/hen.html http://zidian.xpcha.com/heng.html http://zidian.xpcha.com/hong.html http://zidian.xpcha.com/hou.html

​		lpush zidianspider:start_urls  http://zidian.xpcha.com/hu.html http://zidian.xpcha.com/hua.html http://zidian.xpcha.com/huai.html http://zidian.xpcha.com/huan.html http://zidian.xpcha.com/huang.html http://zidian.xpcha.com/hui.html http://zidian.xpcha.com/hun.html http://zidian.xpcha.com/huo.html http://zidian.xpcha.com/ji.html http://zidian.xpcha.com/jia.html http://zidian.xpcha.com/jian.html http://zidian.xpcha.com/jiang.html http://zidian.xpcha.com/jiao.html http://zidian.xpcha.com/jie.html http://zidian.xpcha.com/jin.html http://zidian.xpcha.com/jing.html http://zidian.xpcha.com/jiong.html http://zidian.xpcha.com/jiu.html http://zidian.xpcha.com/ju.html http://zidian.xpcha.com/juan.html http://zidian.xpcha.com/jue.html http://zidian.xpcha.com/jun.html http://zidian.xpcha.com/ka.html http://zidian.xpcha.com/kai.html http://zidian.xpcha.com/kan.html http://zidian.xpcha.com/kang.html http://zidian.xpcha.com/kao.html http://zidian.xpcha.com/ke.html http://zidian.xpcha.com/ken.html http://zidian.xpcha.com/keng.html http://zidian.xpcha.com/kong.html http://zidian.xpcha.com/kou.html http://zidian.xpcha.com/ku.html http://zidian.xpcha.com/kua.html http://zidian.xpcha.com/kuai.html http://zidian.xpcha.com/kuan.html http://zidian.xpcha.com/kuang.html http://zidian.xpcha.com/kui.html http://zidian.xpcha.com/kun.html http://zidian.xpcha.com/kuo.html http://zidian.xpcha.com/la.html http://zidian.xpcha.com/lai.html http://zidian.xpcha.com/lan.html http://zidian.xpcha.com/lang.html http://zidian.xpcha.com/lao.html http://zidian.xpcha.com/le.html http://zidian.xpcha.com/lei.html http://zidian.xpcha.com/leng.html http://zidian.xpcha.com/li.html http://zidian.xpcha.com/lia.html http://zidian.xpcha.com/lian.html http://zidian.xpcha.com/liang.html http://zidian.xpcha.com/liao.html http://zidian.xpcha.com/lie.html http://zidian.xpcha.com/lin.html http://zidian.xpcha.com/ling.html http://zidian.xpcha.com/liu.html http://zidian.xpcha.com/long.html http://zidian.xpcha.com/lou.html http://zidian.xpcha.com/lu.html http://zidian.xpcha.com/lü.html http://zidian.xpcha.com/luan.html http://zidian.xpcha.com/lue.html http://zidian.xpcha.com/lüe.html http://zidian.xpcha.com/lun.html http://zidian.xpcha.com/luo.html http://zidian.xpcha.com/m.html http://zidian.xpcha.com/ma.html http://zidian.xpcha.com/mai.html http://zidian.xpcha.com/man.html http://zidian.xpcha.com/mang.html http://zidian.xpcha.com/mao.html http://zidian.xpcha.com/me.html http://zidian.xpcha.com/men.html http://zidian.xpcha.com/meng.html http://zidian.xpcha.com/mi.html http://zidian.xpcha.com/mian.html http://zidian.xpcha.com/miao.html http://zidian.xpcha.com/mie.html http://zidian.xpcha.com/min.html http://zidian.xpcha.com/ming.html http://zidian.xpcha.com/miu.html http://zidian.xpcha.com/mo.html http://zidian.xpcha.com/mou.html http://zidian.xpcha.com/mu.html http://zidian.xpcha.com/na.html http://zidian.xpcha.com/nai.html http://zidian.xpcha.com/nan.html http://zidian.xpcha.com/nang.html http://zidian.xpcha.com/nao.html http://zidian.xpcha.com/ne.html http://zidian.xpcha.com/nei.html http://zidian.xpcha.com/nen.html http://zidian.xpcha.com/neng.html http://zidian.xpcha.com/ni.html http://zidian.xpcha.com/nian.html http://zidian.xpcha.com/niang.html http://zidian.xpcha.com/niao.html http://zidian.xpcha.com/nie.html http://zidian.xpcha.com/nin.html http://zidian.xpcha.com/ning.html http://zidian.xpcha.com/niu.html http://zidian.xpcha.com/nong.html http://zidian.xpcha.com/nou.html http://zidian.xpcha.com/nu.html http://zidian.xpcha.com/nü.html http://zidian.xpcha.com/nuan.html http://zidian.xpcha.com/nüe.html http://zidian.xpcha.com/nun.html http://zidian.xpcha.com/nuo.html http://zidian.xpcha.com/o.html http://zidian.xpcha.com/ou.html http://zidian.xpcha.com/pa.html http://zidian.xpcha.com/pai.html http://zidian.xpcha.com/pan.html http://zidian.xpcha.com/pang.html http://zidian.xpcha.com/pao.html http://zidian.xpcha.com/pei.html http://zidian.xpcha.com/pen.html http://zidian.xpcha.com/peng.html http://zidian.xpcha.com/pi.html http://zidian.xpcha.com/pian.html

​		lpush zidianspider:start_urls http://zidian.xpcha.com/piao.html http://zidian.xpcha.com/pie.html http://zidian.xpcha.com/pin.html http://zidian.xpcha.com/ping.html http://zidian.xpcha.com/po.html http://zidian.xpcha.com/pou.html http://zidian.xpcha.com/pu.html http://zidian.xpcha.com/qi.html http://zidian.xpcha.com/qia.html http://zidian.xpcha.com/qian.html http://zidian.xpcha.com/qiang.html http://zidian.xpcha.com/qiao.html http://zidian.xpcha.com/qie.html http://zidian.xpcha.com/qin.html http://zidian.xpcha.com/qing.html http://zidian.xpcha.com/qiong.html http://zidian.xpcha.com/qiu.html http://zidian.xpcha.com/qu.html http://zidian.xpcha.com/quan.html http://zidian.xpcha.com/que.html http://zidian.xpcha.com/qun.html http://zidian.xpcha.com/ran.html http://zidian.xpcha.com/rang.html http://zidian.xpcha.com/rao.html http://zidian.xpcha.com/re.html http://zidian.xpcha.com/ren.html http://zidian.xpcha.com/reng.html http://zidian.xpcha.com/ri.html http://zidian.xpcha.com/rong.html http://zidian.xpcha.com/rou.html http://zidian.xpcha.com/ru.html http://zidian.xpcha.com/ruan.html http://zidian.xpcha.com/rui.html http://zidian.xpcha.com/run.html http://zidian.xpcha.com/ruo.html http://zidian.xpcha.com/sa.html http://zidian.xpcha.com/sai.html http://zidian.xpcha.com/san.html http://zidian.xpcha.com/sang.html http://zidian.xpcha.com/sao.html http://zidian.xpcha.com/se.html http://zidian.xpcha.com/sen.html http://zidian.xpcha.com/seng.html http://zidian.xpcha.com/sha.html http://zidian.xpcha.com/shai.html http://zidian.xpcha.com/shan.html http://zidian.xpcha.com/shang.html http://zidian.xpcha.com/shao.html http://zidian.xpcha.com/she.html http://zidian.xpcha.com/shei.html http://zidian.xpcha.com/shen.html http://zidian.xpcha.com/sheng.html http://zidian.xpcha.com/shi.html http://zidian.xpcha.com/shou.html http://zidian.xpcha.com/shu.html http://zidian.xpcha.com/shua.html http://zidian.xpcha.com/shuai.html http://zidian.xpcha.com/shuan.html http://zidian.xpcha.com/shuang.html http://zidian.xpcha.com/shui.html http://zidian.xpcha.com/shun.html http://zidian.xpcha.com/shuo.html http://zidian.xpcha.com/si.html http://zidian.xpcha.com/song.html http://zidian.xpcha.com/sou.html http://zidian.xpcha.com/su.html http://zidian.xpcha.com/suan.html http://zidian.xpcha.com/sui.html http://zidian.xpcha.com/sun.html http://zidian.xpcha.com/suo.html http://zidian.xpcha.com/ta.html http://zidian.xpcha.com/tai.html http://zidian.xpcha.com/tan.html http://zidian.xpcha.com/tang.html http://zidian.xpcha.com/tao.html http://zidian.xpcha.com/te.html http://zidian.xpcha.com/teng.html http://zidian.xpcha.com/ti.html http://zidian.xpcha.com/tian.html http://zidian.xpcha.com/tiao.html http://zidian.xpcha.com/tie.html http://zidian.xpcha.com/ting.html http://zidian.xpcha.com/tong.html http://zidian.xpcha.com/tou.html http://zidian.xpcha.com/tu.html http://zidian.xpcha.com/tuan.html http://zidian.xpcha.com/tui.html http://zidian.xpcha.com/tun.html http://zidian.xpcha.com/tuo.html http://zidian.xpcha.com/wa.html http://zidian.xpcha.com/wai.html http://zidian.xpcha.com/wan.html http://zidian.xpcha.com/wang.html http://zidian.xpcha.com/wei.html http://zidian.xpcha.com/wen.html http://zidian.xpcha.com/weng.html http://zidian.xpcha.com/wo.html http://zidian.xpcha.com/wu.html http://zidian.xpcha.com/xi.html http://zidian.xpcha.com/xia.html http://zidian.xpcha.com/xian.html http://zidian.xpcha.com/xiang.html http://zidian.xpcha.com/xiao.html http://zidian.xpcha.com/xie.html http://zidian.xpcha.com/xin.html http://zidian.xpcha.com/xing.html http://zidian.xpcha.com/xiong.html http://zidian.xpcha.com/xiu.html http://zidian.xpcha.com/xu.html http://zidian.xpcha.com/xuan.html http://zidian.xpcha.com/xue.html http://zidian.xpcha.com/xun.html http://zidian.xpcha.com/ya.html http://zidian.xpcha.com/yan.html http://zidian.xpcha.com/yang.html http://zidian.xpcha.com/yao.html http://zidian.xpcha.com/ye.html http://zidian.xpcha.com/yi.html http://zidian.xpcha.com/yin.html http://zidian.xpcha.com/ying.html http://zidian.xpcha.com/yo.html http://zidian.xpcha.com/yong.html



​	lpush zidianspider:start_urls http://zidian.xpcha.com/you.html http://zidian.xpcha.com/yu.html http://zidian.xpcha.com/yuan.html http://zidian.xpcha.com/yue.html http://zidian.xpcha.com/yun.html http://zidian.xpcha.com/za.html http://zidian.xpcha.com/zai.html http://zidian.xpcha.com/zan.html http://zidian.xpcha.com/zang.html http://zidian.xpcha.com/zao.html http://zidian.xpcha.com/ze.html http://zidian.xpcha.com/zei.html http://zidian.xpcha.com/zen.html http://zidian.xpcha.com/zeng.html http://zidian.xpcha.com/zha.html http://zidian.xpcha.com/zhai.html http://zidian.xpcha.com/zhan.html http://zidian.xpcha.com/zhang.html http://zidian.xpcha.com/zhao.html http://zidian.xpcha.com/zhe.html http://zidian.xpcha.com/zhei.html http://zidian.xpcha.com/zhen.html http://zidian.xpcha.com/zheng.html http://zidian.xpcha.com/zhi.html http://zidian.xpcha.com/zhong.html http://zidian.xpcha.com/zhou.html http://zidian.xpcha.com/zhu.html http://zidian.xpcha.com/zhua.html http://zidian.xpcha.com/zhuai.html http://zidian.xpcha.com/zhuan.html http://zidian.xpcha.com/zhuang.html http://zidian.xpcha.com/zhui.html http://zidian.xpcha.com/zhun.html http://zidian.xpcha.com/zhuo.html http://zidian.xpcha.com/zi.html http://zidian.xpcha.com/zong.html http://zidian.xpcha.com/zou.html http://zidian.xpcha.com/zu.html http://zidian.xpcha.com/zuan.html http://zidian.xpcha.com/zui.html http://zidian.xpcha.com/zun.html http://zidian.xpcha.com/zuo.html
```

数据库：

```mysql
DROP TABLE IF EXISTS `zidian`;
CREATE TABLE `zidian` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `zi` varchar(255) DEFAULT '',
  `thumb` varchar(255) DEFAULT '',
  `pinyin` varchar(255) DEFAULT '',
  `wuxing` varchar(255) DEFAULT '',
  `jiegou` varchar(255) DEFAULT '',
  `bushou` varchar(255) DEFAULT '',
  `bihua` (255) DEFAULT '',
  `request` varchar(255) DEFAULT '',
  `base` text,
  `kangxi` varchar(255) DEFAULT '',
  `guhanyu` text,
  `xiangxi` text,
  `develop` text,
  PRIMARY KEY (`id`),
  KEY `zi` (`zi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

   程序端执行: scrapy runspider feng.py
   提取至mysql数据库 : 	      

​	执行 

```python
		python process_item_item_mysql.py
```

​	

> 声明：此类项目仅供个人学习。
>
> ​	不要对压力测试太过迷恋，除非对方抢了你的糖果！                    -----------------《黑客守则》
