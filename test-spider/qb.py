# -*- coding: utf-8 -*-    
#qb.py
     
import urllib2    
import urllib    
import re    
import thread    
import time    
  
    
#----------- 加载处理糗事百科 -----------    
class Spider_Model:    
        
    def __init__(self):    
        self.page = 1    
        self.pages = []    
        self.enable = False    
    
    # 将所有的段子都扣出来，添加到列表中并且返回列表    
    def GetPage(self,page):    
        myUrl = "http://m.qiushibaike.com/hot/page/" + page    
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
        headers = { 'User-Agent' : user_agent }   
        req = urllib2.Request(myUrl, headers = headers)   
        myResponse = urllib2.urlopen(req)  
        myPage = myResponse.read()    
        #encode的作用是将unicode编码转换成其他编码的字符串    
        #decode的作用是将其他编码的字符串转换成unicode编码    
        unicodePage = myPage.decode("utf-8")    
    
        # 找出所有class="content"的div标记    
        #re.S是任意匹配模式，也就是.可以匹配换行符  
        #print unicodePage  
        #######替换#########  
        myItems = re.findall('<div.*?class="content".*?>.*?<span>.*?(.*?)</span>',unicodePage,re.S)    
        #######替换#########  
        items = []    
        for item in myItems:    
            #items.append([item[0].replace("\n",""),item[1].replace("\n","")])  
            #######替换#########  
            items.append(item)
            #######替换#########  
        return items    
    
    # 用于加载新的段子    
    def LoadPage(self):    
        # 如果用户未输入quit则一直运行    
        while self.enable:    
            # 如果pages数组中的内容小于2个    
            if len(self.pages) < 2:    
                try:    
                    # 获取新的页面中的段子们    
                    myPage = self.GetPage(str(self.page))    
                    self.page += 1    
                    self.pages.append(myPage)    
                except:    
                    print '无法链接糗事百科！'    
            else:    
                time.sleep(1)    
            
    def ShowPage(self,nowPage,page):    
        for items in nowPage:    
            #print u'第%d页' % page , items[0]  , items[1]    
            #######替换#########  
            print u'第%d页' % page , items   
            #######替换#########  
            myInput = raw_input()    
            if myInput == "quit":    
                self.enable = False    
                break    
            
    def Start(self):    
        self.enable = True    
        page = self.page    
    
        print u'正在加载中请稍候......'    
            
        # 新建一个线程在后台加载段子并存储    
        thread.start_new_thread(self.LoadPage,())    
            
        #----------- 加载处理糗事百科 -----------    
        while self.enable:    
            # 如果self的page数组中存有元素    
            if self.pages:    
                nowPage = self.pages[0]    
                del self.pages[0]    
                self.ShowPage(nowPage,page)    
                page += 1    
    
    
#----------- 程序的入口处 -----------    
print u"""  
======================================
糗百爬虫修复版本

======================================
修改前:
第1页 分享到微信" rel="nofollow 微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a> 

======================================
对新的页面节点正则匹配进行修改:
新的页面节点如下:
<div class="content">
<span>上小学有一次和同桌妹子打架，楼主输了。上了两节课，楼主就忘了这事，继续和同桌嘻嘻哈哈的玩耍。。。<br/>放学时，楼主忽然想起同桌打我的事，就对同桌说：放学后，你在校门口等一下。同桌：咋了？<br/>楼主：你今天打疼我了，放学后，我得让我哥打你啊。。。<br/>同桌一脸懵哔的点点头。后来，后来，我和我哥鼻青脸肿的不敢回家。。。</span>

新的匹配方式如下:
re.findall('<div.*?class="content".*?>.*?<span>.*?(.*?)</span>',unicodePage,re.S) 


======================================
修改后:
第1页 办假证的。

第1页 是你的童年，请点赞

第1页 有个同事少白头。所以看起来比实际年龄要大。大家都劝他去染 发。<br/>他回答道:我才不去染，我这个样子跟老婆逛街，大家都羡慕我老 牛 吃 嫩 草！

第1页 菩提开花，所遇有缘人一世安好！

第1页 老婆出差，送老婆去车站，本想送到站里面的，谁知检票员不让进，老婆在里面瞅了瞅我哈哈大笑道:尼玛，来呀，来打我啊！你进不来！<br/>知道老婆一直是个二货的我无奈的笑笑，谁知检票员开口了:你进去吧！这次给你个特例！

第1页 女儿看她小时候的照片，都没有头发，然后摸了摸自己的小辫子，喃喃的说：“原来我小时候是男生，后来才长成女生的。。。。。”。。。。。
======================================
"""  
    
    
print u'请按下回车浏览今日的糗百内容：'    
raw_input(' ')    
myModel = Spider_Model()    
myModel.Start() 