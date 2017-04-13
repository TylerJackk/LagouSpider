# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from LagouSpider.items import JobItem
from LagouSpider.settings import *


class LagouSpider(scrapy.Spider):
	name = "lagou"
	allowed_domains = ["lagou.com"]
	start_urls = ["https://www.lagou.com/zhaopin/"]

	def __init__(self, *arg, **kwargs):
		self.headers = HEADERS
		self.jobs = JOBS
		self.job = ''

	def start_requests(self):
		for job in self.jobs:
			self.job = job
			for page_num in range(1, 31):
				url = (self.start_urls[0] + str(job) + "/" + str(page_num) + "/")
				yield Request(url, callback=self.make_url)

	def make_url(self, response):
		soup = BeautifulSoup(response.body, "lxml")
		for url in soup.find_all("a", "position_link"):
			job_url = url['href']  # 职位详情的url
			yield self.make_requests_from_url(job_url)

	def parse(self, response):
		item = JobItem()
		soup = BeautifulSoup(response.body, "lxml")
		soup.prettify("utf-8")
		item['positionName'] = soup.find("div", class_="job-name")['title']
		a = list(soup.find("dd", class_="job_request").stripped_strings)  # 经验 学历
		item['jobType'] = self.job
		item['url'] = response.url
		item['salary'] = a[0]
		item['city'] = a[1][1:-1]
		item['workYear'] = a[2][:-1]
		item['education'] = a[3][:-1]
		item['jobNature'] = a[4]
		item['companyName'] = soup.find("img", class_="b2")['alt']
		job_detail = list(soup.find("dd", class_="job_bt").stripped_strings)
		item['jobDetail'] = ''.join(job_detail)
		a = list(soup.find("ul", class_="c_feature").stripped_strings)
		item['industryField'] = a[0]
		item['financeStage'] = a[2]
		if len(a) == 10:
			item['financeOrg'] = a[4]
			item['companySize'] = a[6]
			item['companyWebSite'] = a[8]
		if len(a) == 8:
			item['financeOrg'] = 'null'
			item['companySize'] = a[4]
			item['companyWebSite'] = a[6]
		item['positionAdvantage'] = list(soup.find("dd", class_="job-advantage").stripped_strings)[1]
		work_addr = list(soup.find("div", class_="work_addr").stripped_strings)
		if len(work_addr) != 2:
			item['district'] = work_addr[2]
		else:
			item['district'] = work_addr[0][2:]
		item['positionId'] = soup.select("#jobid")[0]['value']
		item['companyId'] = soup.select("#companyid")[0]['value']
		return item
