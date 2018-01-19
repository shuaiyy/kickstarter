#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : run_spider_with_psutil.py
# @Author: Shuaiyy
# @Date  : 2018/1/4 17:25
# @Desc  : 

import psutil
import subprocess
import time
import sys


def run():
    timeout = 60*5
    stop_time = time.time() + timeout  # 1.5h后的时间戳
    python = r'D:\ProgramData\Anaconda2\python.exe'
    script = r'D:\mypy\kickstarter\kickstarter\run_spider.py'
    cmd = '{} {}'.format(python, script)
    cmd = 'scrapy crawl stupid_spider'
    # sub = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    sub = subprocess.Popen(cmd, shell=True) # 在cmd/shell里显示输出
    while (stop_time - time.time()) > 0:
        if not psutil.pid_exists(sub.pid):  # 爬虫进程结束后自动退出
            sys.exit(0)
        time.sleep(60*2)  # 2分钟检查一次
    # timeout后手动杀死爬虫
    if psutil.pid_exists(sub.pid):
        psutil.Process(sub.pid).terminate()
        # psutil.Process(sub.pid).terminate()
        print '\nkill\n'
    if psutil.pid_exists(sub.pid):
        print 'kill failed!'
        sys.exit(0)

if __name__ == '__main__':
    run()


