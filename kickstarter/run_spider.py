#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : run_spider.py
# @Author: Shuaiyy
# @Date  : 2017/12/30 13:35
# @Desc  : 
from scrapy.cmdline import execute
import time
import sys
import os


def main():
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(["scrapy", "crawl", "description_spider"])
    # 上面的语句执行完成就退出了。。。
    time.sleep(60*4)
    execute(["scrapy", "crawl", "community_spider"])
    time.sleep(60*4)
    execute(["scrapy", "crawl", "reward_spider"])
    time.sleep(60*4)
    execute(["scrapy", "crawl", "live_outdate_spider"])
    time.sleep(60 * 4)
    execute(["scrapy", "crawl", "new_project_spider"])
    time.sleep(60 * 4)


if __name__ == '__main__':
    main()
    "/usr/bin/python  /home/ubuntu/kickstarter/run_spider.py"
    "cd /home/ubuntu/kickstarter && /usr/local/bin/scrapy crawl new_project_spider > /dev/null 2>&1 & "