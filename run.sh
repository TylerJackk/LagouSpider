#!/bin/bash

export PATH=$PATH:/usr/local/bin

source  /home/ubuntu/lagouenv/bin/activate

cd /home/ubuntu/LagouSpider/LagouSpider

nohup scrapy crawl lagou >> example.log 2>&1 &