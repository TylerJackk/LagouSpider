# -*- coding: utf-8 -*-
from scrapy import cmdline


def run():
	cmdline.execute("scrapy crawl lagou".split())

if __name__ == '__main__':
	run()
