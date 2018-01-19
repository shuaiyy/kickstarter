# -*- coding: utf-8 -*-
import scrapy
from ..util.mongo import MongoOperate
from ..items import CommunityItem


class CommunitySpiderSpider(scrapy.Spider):
    name = "community_spider"
    allowed_domains = ["kickstarter.com"]
    start_urls = (
        'https://www.kickstarter.com',
    )

    def parse(self, response):
        community_tasks = MongoOperate().get_community_task()
        for id, url in community_tasks:
            yield scrapy.Request(url=url, meta={'id': id}, callback=self.parse_community)

    def parse_community(self, response):
        item = CommunityItem()
        item['id'] = response.meta.get('id', -1)
        item['new_backers_count'] = int(response.css('div.new-backers div.count::text'
                                                     ).extract_first(default='0').replace(',',''))
        item['return_backers_count'] = int(response.css('div.existing-backers  div.count::text'
                                                        ).extract_first(default="0").replace(',', ''))
        yield item
