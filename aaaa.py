#coding:utf-8
import threading
#在项目外用脚本启动爬虫 
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
import qiushibaike.qiushibaike.items
from qiushibaike.qiushibaike.spiders.csbk import Csbk
from qiushibaike.qiushibaike.pipelines import QiushibaikePipeline
from scrapy.settings import Settings

#配置文件在这里手动实现 
#下面是官方说法  
#Running spiders outside projects it’s not much different. 
#You have to create a generic Settings object and populate it as needed (See 内置设定参考手册 for the available settings), 
#instead of using the configuration returned by get_project_settings. 
#翻译 
#运行蜘蛛外项目没有多少不同。
#你必须根据需要创建一个通用设置对象并填充它(见内置设定参考手册可用的设置),而不是使用配置由get_project_settings返回。
def aaa():
	settings = Settings({
		#Spiders can still be referenced by their name if SPIDER_MODULES is set with the modules where Scrapy should look for spiders.
		#Otherwise, passing the spider class as first argument in the CrawlerRunner.
		#翻译
		#蜘蛛仍然可以引用他们的名字如果SPIDER_MODULES设置模块,Scrapy应该找蜘蛛。
		#否则,将蜘蛛CrawlerRunner类作为第一个参数。
		'SPIDER_MODULES':['qiushibaike.qiushibaike.spiders.csbk'],  

		'ROBOTSTXT_OBEY':True,
		#设置包头
		'DEFAULT_REQUEST_HEADERS':{
		'Referer':'http://www.qiushibaike.com/text/',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'},
		#启用pipelines组件
		'ITEM_PIPELINES':{
	    'qiushibaike.qiushibaike.pipelines.QiushibaikePipeline': 400,}
	    })
	runner=CrawlerRunner(settings)

	d=runner.crawl('Csbk')
	d.addBoth(lambda _: reactor.stop())
	reactor.run()
	return 0
def thread_qiushi():
	print("--------------")
	threading.Thread(target=aaa())





