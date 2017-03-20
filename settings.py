BOT_NAME = 'qiushibaike'

SPIDER_MODULES = ['qiushibaike.spiders']
NEWSPIDER_MODULE = 'qiushibaike.spiders'

MYSQL_HOST='localhost'
MYSQL_DBNAME='duanzhi'
MYSQL_USER='root'
MYSQL_PASSWD='213314'
MYSQL_PORT=3306

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