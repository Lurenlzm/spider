# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from qiushibaike.qiushibaike.items import QiushibaikeItem

class QiushibaikePipeline(object):
	def __init__(self):
		self.connect=pymysql.connect(
			host='localhost',
			user='root',
			passwd='213314',
			charset='utf8'
			)
		self.cursor=self.connect.cursor()
		self.cursor.execute("TRUNCATE TABLE duanzhi.`csbk`")
#
	def process_item(self, item, spider):
		sql="INSERT INTO duanzhi.`csbk`(TEXT) VALUES (%s)"
		self.cursor.execute(sql,item['text'])
		self.connect.commit()
		return item
