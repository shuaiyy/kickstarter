#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : red.py
# @Author: Shuaiyy
# @Date  : 2018/1/18 17:00
# @Desc  : 

import requests
from scrapy import Selector
from bs4 import BeautifulSoup
import json

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

if __name__ == '__main__':
    sess = requests.Session()
    html = sess.get('https://www.hoomxb.com/plan/444', headers=DEFAULT_REQUEST_HEADERS).text
    # <meta name="csrf-token" content="rBtV7lU6-Zwdd7SfgmRTdsbpCxhDR2qgfY4g">
    csrf = Selector(text=html).css('meta[name=csrf-token]::attr(content)').extract_first()
    csrf2 = BeautifulSoup(html, "lxml").select('meta[name=csrf-token]')[0].get('content')
    print csrf2, csrf == csrf2
    if csrf:
        DEFAULT_REQUEST_HEADERS['X-CSRF-Token'] = csrf
    html2 = sess.post('https://www.hoomxb.com/api/plan/joinRecord', headers=DEFAULT_REQUEST_HEADERS, data={'id': 444}).text
    d = json.loads(html2)
    print len(d)
    print d
    for x in d:
        print x, d[x]
