# -*- coding: utf-8 -*-

BOT_NAME = 'LagouSpider'

SPIDER_MODULES = ['LagouSpider.spiders']
NEWSPIDER_MODULE = 'LagouSpider.spiders'


HEADERS = {	"Host": "www.lagou.com",
			"Upgrade-Insecure-Requests": "1",
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Connection":"keep-alive"}

#
JOBS = {"Java", "Python", "PHP", "C++", "shujuwajue", "HTML5", "Android", "iOS", "webqianduan"}

COOKIES_ENABLES = False
AUTOTHROTTLE_ENABLED = True  # 限速
AUTOTHROTTLE_START_DELAY = 5.0  # 默认5.0
DOWNLOAD_DELAY = 3

ROBOTSTXT_OBEY = True


# 数据库配置
MYSQL_HOST = 'xxx.xx.xx.xx'
MYSQL_DBNAME = 'Spider'
MYSQL_USER = 'xx'
MYSQL_PASSWD = 'xx'
MYSQL_PORT = 0

ITEM_PIPELINES = {
	'LagouSpider.pipelines.LagouspiderPipeline': 300,
}


# 邮件配置
From_ADDR = 'xxx@xx.com'
TO_ADDR = 'xxx@xx.com'
PASSWORD = 'xxxx'
SMTP = 'smtp.163.com'