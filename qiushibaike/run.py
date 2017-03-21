# coding:utf-8

#在项目内用脚本启动爬虫
#代码如下，不过用这个项目直接运行是不行的
#首先 这个项目没有配置文件（settings.py） 因为爬虫是在项目外运行的，配置文件在项目外的脚本中直接写的，具体看spider/ Run.py
#其次 这个项目中的csbk.py中导入模块的路径是相对与spider/Run.py的路径；而如果要在项目内启动爬虫的话，应该把路径改一下，具体看哪里报错改哪里。
#     例如 ：from qiushibaike.qiushibaike.items import QiushibaikeItem   应该改为  from qiushibaike.items import QiushibaikeItem


#本项目的settings.py文件配置 
"""
BOT_NAME = 'qiushibaike'

SPIDER_MODULES = ['qiushibaike.spiders']
NEWSPIDER_MODULE = 'qiushibaike.spiders'


ITEM_PIPELINES = {
    'qiushibaike.pipelines.QiushibaikePipeline': 301,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qiushibaike (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DEFAULT_REQUEST_HEADERS = {
	'Referer':'http://www.qiushibaike.com/text/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

你也可以根据实际进行改动   参考官方文档  """

#from scrapy import cmdline
#def updata():
	#cmdline.execute("scrapy crawl Csbk".split())
	#return 0
#if __name__ == '__main__':
	#updata()

