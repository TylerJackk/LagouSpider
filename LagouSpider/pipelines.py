# -*- coding: utf-8 -*-

import MySQLdb
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
import datetime
from envelopes import Envelope

settings = get_project_settings()


class LagouspiderPipeline(object):
	def __init__(self):
		self.ids_seen = set()
		self.conn = MySQLdb.connect(user=settings['MYSQL_USER'], passwd=settings['MYSQL_PASSWD'],
									db=settings['MYSQL_DBNAME'],
									host=settings['MYSQL_HOST'], port=settings['MYSQL_PORT'], charset="utf8")
		self.cursor = self.conn.cursor()
		self.conn.commit()

	def process_item(self, item, spider):
		curTime = datetime.datetime.now()
		try:
			self.cursor.execute("""INSERT INTO t_position (t_url,t_type,t_company_id, t_company_name, t_company_size, t_company_website, t_position_id, t_position_name, t_work_year,t_education,
	t_jobnature,t_salary,t_finance_stage,t_finance_org,t_industry_field,t_publish_time,t_position_advantage,t_city,t_district,t_job_detail)
									VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
								(
									item['url'].encode('utf-8'),
									item['jobType'].encode('utf-8'),
									item['companyId'].encode('utf-8'),
									item['companyName'].encode('utf-8'),
									item['companySize'].encode('utf-8'),
									item['companyWebSite'].encode('utf-8'),
									item['positionId'].encode('utf-8'),
									item['positionName'].encode('utf-8'),
									item['workYear'].encode('utf-8'),
									item['education'].encode('utf-8'),
									item['jobNature'].encode('utf-8'),
									item['salary'].encode('utf-8'),
									item['financeStage'].encode('utf-8'),
									item['financeOrg'].encode('utf-8'),
									item['industryField'].encode('utf-8'),
									curTime,
									item['positionAdvantage'].encode('utf-8'),
									item['city'].encode('utf-8'),
									item['district'].encode('utf-8'),
									item['jobDetail'].encode('utf-8')
								)
								)

			self.conn.commit()
		except MySQLdb.Error as e:
			raise DropItem()
		return item

	def open_spider(self, spider):
		self.start_time = datetime.datetime.now()

	def close_spider(self, spider):
		analysis = spider.crawler.stats.get_stats()
		scrapyed_item = 0
		if analysis.get('item_scraped_count') != None:
			scrapyed_item = analysis['item_scraped_count']
		self.end_time = datetime.datetime.now()

		total_time = self.end_time - self.start_time
		text_body = '爬取职位' + str(scrapyed_item) + '个,用时' + str(total_time)
		envelope = Envelope(
			from_addr=(settings['FROM_ADDR'], u'Lagou爬虫'),
			to_addr=(settings['TO_ADDR'], u'收件人'),
			subject=u'今日爬虫完成',
			text_body=text_body
		)
		envelope.send(settings['SMTP'], login=settings['FROM_ADDR'],
					  password=settings['PASSWORD'], tls=True)

