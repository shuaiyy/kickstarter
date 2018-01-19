# -*- coding: utf-8 -*-
import scrapy
from ..items import StupidKickstarterItem
import json
from ..util.mongo import MongoOperate

class ProfileSpiderSpider(scrapy.Spider):
    name = "profile_spider"
    allowed_domains = ["kickstarter.com"]
    start_urls = (
        'http://www.kickstarter.com/',
    )

    def parse(self, response):
        usernames = MongoOperate().get_users()
        profile_url = r'https://www.kickstarter.com/profile/{}/'
        for usename in usernames:
            profile_url = r'https://www.kickstarter.com/profile/{}/'.format(usename)
            headers = {
                'referer': profile_url,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
            }
            yield scrapy.Request(url=profile_url, headers=headers, callback=self.get_project)

    def get_project(self, response):
        datas = response.css('div.react-user-prof-card ::attr(data-project) ').extract()
        for data in datas:
            item = StupidKickstarterItem()
            data = json.loads(data)
            keys = item.field_keys()
            for k in data:
                if k in keys:
                    item[k] = data[k]
            yield item
