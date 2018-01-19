# -*- coding: utf-8 -*-
import scrapy
from ..util.kickurls import make_urls_for_new
from ..items import StupidKickstarterItem
import json


class NewProjectSpiderSpider(scrapy.Spider):
    name = "new_project_spider"
    allowed_domains = ["kickstarter.com"]
    start_urls = make_urls_for_new()

    def parse(self, response):
        data_projects = response.css('div[data-project]::attr(data-project)').extract()
        # print len(data_projects)
        for data_project in data_projects:
            # print data_project
            item = StupidKickstarterItem()
            keys = item.field_keys()
            data = json.loads(data_project)
            for k in data:
                if k in keys:
                    item[k] = data[k]
            yield item
