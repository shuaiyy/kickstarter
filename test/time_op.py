#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : time_op.py
# @Author: Shuaiyy
# @Date  : 2018/1/17 15:31
# @Desc  : 

import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    # 时间字符串
    time_str = '2018-01-15 15:27:54'
    # 字符串的time format
    time_fmt = '%Y-%m-%d %H:%M:%S'
    # 转换成时间数组, str parse time
    time_array = time.strptime(time_str, time_fmt)
    print time_array
    # str from time, 时间数组转字符串
    time_str = time.strftime(time_fmt, time_array)
    print time_str
    # 默认时间为当前时间
    time_str = time.strftime(time_fmt)
    print time_str

    # 当前时间的时间戳，秒，3位小数
    timestamp = time.time()
    print timestamp
    # 时间数组转换为时间戳
    timestamp = time.mktime(time_array)
    print timestamp
    # 时间戳转换为当地时间，然后在格式化成字符串
    localtime = time.localtime(timestamp)
    print localtime  # 时间数组
    time_str = time.strftime(time_fmt, localtime)
    print time_str
    # 获取当前时间
    time_now = time.time()
    # 转换成localtime
    time_local = time.localtime(time.time())
    # 转换成新的时间格式(2018-01-15 15:27:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    print dt
if __name__ == '__main__':
    main()


