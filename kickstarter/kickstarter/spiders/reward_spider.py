# -*- coding: utf-8 -*-
import HTMLParser
import json
import scrapy
from ..items import RewardItem
from ..util.mongo import MongoOperate


class RewardSpiderSpider(scrapy.Spider):
    name = "reward_spider"
    allowed_domains = ["kickstarter.com"]
    start_urls = MongoOperate().get_rewards_task()

    def parse(self, response):
        h = HTMLParser.HTMLParser()
        current_project = response.css('script').re(r'window\.current_project.+?"(\{.+?\})";')[0]
        # current_project = current_project.replace('\n', '').replace(r'\\\\\\\\"', "")
        current_project = current_project.replace('\n', '').replace('\\\\"', "'")
        current_project = h.unescape(current_project)
        # print current_project
        cp = json.loads(current_project)
        item = RewardItem()
        item['id'] = cp.get('id', -1)
        item['rewards'] = cp.get('rewards', [])
        item['rewards_level'] = len(item['rewards']) - 1
        item['updates_count'] = cp.get('updates_count', 0)
        item['comments_count'] = cp.get('comments_count', 0)
        item['video'] = cp.get('video', False)
        item['is_first_creator'] = len(response.selector.re(r'.*?(First.*?created).*?')) > 0
        yield item
