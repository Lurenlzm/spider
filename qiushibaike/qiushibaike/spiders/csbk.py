#coding:utf-8
import scrapy 
from scrapy.spiders import CrawlSpider,Request,Rule
from qiushibaike.qiushibaike.items import QiushibaikeItem
from scrapy.linkextractors import LinkExtractor

class Csbk(CrawlSpider):
	name='Csbk'    #这个必须写 
	allowed=['http://www.qiushibaike.com']    #限制爬虫爬取的范围  
	def start_requests(self):   #生成爬虫爬取的链接  
		urls="http://www.qiushibaike.com/text/"
		yield Request(url=urls,callback=self.parse)
		for i in range(1,6):
			url ="http://www.qiushibaike.com/text/page/"+str(i)+"/?s=4964137"
			yield Request(url=url, callback=self.parse)
	def parse(self,response):   #处理爬取到的网页数据   
		print('____________________________________')
		print(response.url)
		item=QiushibaikeItem()
		content=response.xpath('//*[@class="content-block clearfix"]/div[@id="content-left"]/div[@class="article block untagged mb15"]')
		print(len(content))
		num=0
		for x in xrange(1,len(content)):
			item['text']="".join(response.xpath('//*[@class="content-block clearfix"]/div[@id="content-left"]/div[@class="article block untagged mb15"]['+str(x)+
							']/a[@target="_blank"]/div[@class="content"]/span/text()').extract()).encode('utf-8')
			print('===========')
			print(len(item['text']))
			print(item['text'])
			yield item