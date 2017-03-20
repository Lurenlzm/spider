# coding:utf-8

#在项目内用脚本启动爬虫 
from scrapy import cmdline
def updata():
	cmdline.execute("scrapy crawl Csbk".split())
	return 0
if __name__ == '__main__':
	updata()

