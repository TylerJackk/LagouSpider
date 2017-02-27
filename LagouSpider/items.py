# -*- coding: utf-8 -*-
import scrapy


class JobItem(scrapy.Item):
	url = scrapy.Field()
	jobType = scrapy.Field()
	companyId = scrapy.Field()
	companyName = scrapy.Field()
	companySize = scrapy.Field()
	companyWebSite = scrapy.Field()
	positionId = scrapy.Field()
	positionName = scrapy.Field()
	workYear = scrapy.Field()
	jobDetail = scrapy.Field()
	education = scrapy.Field()
	financeOrg = scrapy.Field()
	jobNature = scrapy.Field()  # 全职 实习
	salary = scrapy.Field()
	financeStage = scrapy.Field()
	industryField = scrapy.Field()
	publishTime = scrapy.Field()
	positionAdvantage = scrapy.Field()
	city = scrapy.Field()
	district = scrapy.Field()
