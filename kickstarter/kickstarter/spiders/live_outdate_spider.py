# -*- coding: utf-8 -*-
import HTMLParser
import json
import scrapy
from ..items import OutdateItem
from ..util.mongo import MongoOperate


class LiveOutdateSpiderSpider(scrapy.Spider):
    name = "live_outdate_spider"
    allowed_domains = ["kickstarter.com"]
    start_urls = MongoOperate().get_outdate_task()
    
    keys = ['deadline', 'id', 'state_changed_at', 'goal', 'pledged', 'state',
            'converted_pledged_amount', 'backers_count',
    ]

    def parse(self, response):
        h = HTMLParser.HTMLParser()
        current_project = response.css('script').re(r'window\.current_project.+?"(\{.+?\})";')[0]
        # current_project = current_project.replace('\n', '').replace(r'\\\\\\\\"', "")
        current_project = current_project.replace('\n', '').replace('\\\\"', "'")
        current_project = h.unescape(current_project)
        # print current_project
        cp = json.loads(current_project)
        item = OutdateItem()
        for k in self.keys:
            item[k] = cp.get(k)
        yield item
