# LagouSpider
## 项目简介
基于scrapy的[拉勾网](https://www.lagou.com/)爬虫，抓取各种职位的信息，并存储在MySQL数据库中。

## 功能介绍
1. 自定义爬取的职位
2. 存储到MySQL数据库
3. 部署在服务器，每天定时执行，完成后发送邮件报告

## 使用方法
### Python环境
	2.7.10
### 依赖包
安装requirements.txt依赖
	
	pip install -r requirements.txt 
### 文件配置(settings.py)

设置要爬取的职位,格式严格按照拉勾网URL

例如:https://www.lagou.com/zhaopin/**ziranyuyanchuli**/2/

	JOBS = {"Java", "Python", "PHP", "C++", "shujuwajue", "HTML5", "Android", "iOS", "webqianduan"}

	# 执行create_table.sql
	# 数据库配置
	MYSQL_HOST = 'xxx.xx.xx.xx'
	MYSQL_DBNAME = 'Spider'
	MYSQL_USER = 'xx'
	MYSQL_PASSWD = 'xx'
	MYSQL_PORT = 0
	
	# 邮件配置
	From_ADDR = 'xxx@xx.com'
	TO_ADDR = 'xxx@xx.com'
	PASSWORD = 'xxxx'
	SMTP = 'smtp.163.com'

## 运行
	scrapy crawl lagou
	
or

	python main.py
	
## Linux部署
virtualenv创建环境

修改run.sh，设置virtualenv路径和scrapy路径

	#!/bin/bash

	export PATH=$PATH:/usr/local/bin

	source  /home/ubuntu/lagouenv/bin/activate
	cd /home/ubuntu/LagouSpider/LagouSpider

	nohup scrapy crawl lagou >> example.log 2>&1 &
配置crontab每日定时运行

	15 09  * * * (source /home/ubuntu/LagouSpider/LagouSpider/run.sh)

## 职位分析
实现中