#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : wxy.py
# @Author: Shuaiyy
# @Date  : 2018/1/16 15:38
# @Desc  : 

import sys
import requests
from scrapy import Selector

reload(sys)
sys.setdefaultencoding('utf-8')

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'http://www.weixueyuan.net/',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

def parse_article(article_url):
    s = Selector(text=requests.get(url=article_url, headers=DEFAULT_REQUEST_HEADERS).content)
    text = s.css('#art-body').extract_first()
    text = text.replace('src="/uploads', 'src="http://www.weixueyuan.net/uploads')
    title = s.css('#article h1').extract_first()
    return '\n{}\n{}\n'.format(title, text)


def parse_list(url):
    s = Selector(text=requests.get(url=url, headers=DEFAULT_REQUEST_HEADERS).content)
    list_a = s.css('#art-list dd  a::attr(href)').extract()
    urls = []
    for i in list_a:
        urls.append('http://www.weixueyuan.net'+ i)
    return urls

if __name__ == '__main__':
    # t = parse_article('')
    # print t
    # l = parse_list('http://www.weixueyuan.net/java/rumen_1/')
    for i in range(1, 14):
        with open('rumen_{}.html'.format(i), 'a') as f:
            l = parse_list('http://www.weixueyuan.net/java/rumen_{}/'.format(i))
            for url_ in l:
                text = parse_article(url_)
                f.write(text)
                f.write('\n'+ url_)


