#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : test.py
# @Author: Shuaiyy
# @Date  : 2017/12/31 17:59
# @Desc  :  爬取reward数据,资助不同金额得到的奖励不同
# url: https://www.kickstarter.com/projects/1000576969/the-math-chef/rewards

import scrapy
import cPickle as pickle
import json
import HTMLParser
from ..items import StupidKickstarterItem
import json


class RewardSpider(scrapy.Spider):

    name = "stupid_spider1"
    allowed_domains = ["kickstarter.com"]
    start_urls = (
        'https://www.kickstarter.com/projects/1000576969/the-math-chef/rewards',
    )

    def parse(self, response):
        h = HTMLParser.HTMLParser()
        current_project = response.css('script').re(r'window\.current_project.+?"(\{.+?\})";')
        current_project = current_project.replace('\n', '').replace('\\\\\\\\"', ' ')
        current_project = h.unescape(current_project)
        current_project = json.loads(current_project)
        cp = current_project
        # 改这里
        RewardItem = dict
        # id = Field()
        # rewards = Field()
        # failed_at = Field()  # 如果是成功的项目呢
        # items = Field()
        # updates_count = Field()
        # comments_count = Field()
        # video = Field() # 这个字段是的意义占不清楚
        item = RewardItem()
        item['id'] = cp.get('id', -1)
        item['rewards'] = cp.get('rewards', [])
        item['updates_count'] = cp.get('updates_count')
        item['comments_count'] = cp.get('comments_count')
        item['video'] = cp.get('video')
        item['is_first_creator'] = len(response.selector.re(r'.*?(First.*?created).*?')) > 0
        yield item
        for k, v in item.iteritems():
            print k, '    :   ', v


class CommentSpider(scrapy.Spider):

    name = "stupid_spider1"
    allowed_domains = ["kickstarter.com"]
    start_urls = (
        'https://www.kickstarter.com/projects/1000576969/the-math-chef/comments',
    )

    def parse(self, response):
        for s_url in response.css('ol.list-comments a').re(r'".*?(/profile/.+?)"'):
            user_profile = response.urljoin(s_url)
            # 改这里
            RewardItem = dict
            # id = Field()
            # rewards = Field()
            # failed_at = Field()  # 如果是成功的项目呢
            # items = Field()
            # updates_count = Field()
            # comments_count = Field()
            # video = Field() # 这个字段是的意义占不清楚
            item = RewardItem()
            item['url'] = None
            yield item
            yield scrapy.Request(url=user_profile)



class ProjectSpider(scrapy.Spider):

    name = "stupid_spider1"
    allowed_domains = ["kickstarter.com"]
    start_urls = (
        'https://www.kickstarter.com/projects/1000576969/the-math-chef/rewards',
    )

    def parse(self, response):
        h = HTMLParser.HTMLParser()
        current_project = response.css('script').re(r'window\.current_project.+?"(\{.+?\})";')[0]
        current_project = current_project.replace('\n', '').replace('\\\\\\\\"', ' ')
        current_project = h.unescape(current_project)
        current_project = json.loads(current_project)
        cp = current_project
        # 改这里
        RewardItem = dict
        # id = Field()
        # rewards = Field()
        # failed_at = Field()  # 如果是成功的项目呢
        # items = Field()
        # updates_count = Field()
        # comments_count = Field()
        # video = Field() # 这个字段是的意义占不清楚
        item = RewardItem()
        item['id'] = cp.get('id', -1)
        item['rewards'] = cp.get('rewards', [])
        item['updates_count'] = cp.get('updates_count')
        item['comments_count'] = cp.get('comments_count')
        item['video'] = cp.get('video')
        yield item
        for k, v in item.iteritems():
            print k, '    :   ', v


class CommunitySpider(scrapy.Spider):

    name = "stupid_spider1"
    allowed_domains = ["kickstarter.com"]
    start_urls = (
        'https://www.kickstarter.com/projects/952823766/electro-pop-band-nans-and-nat-make-their-debut-alb/community',
    )

    def parse(self, response):
        h = HTMLParser.HTMLParser()
        current_project = response.css('script').re(r'window\.current_project.+?"(\{.+?\})";')[0]
        current_project = current_project.replace('\n', '').replace('\\\\\\\\"', ' ')
        current_project = h.unescape(current_project)
        current_project = json.loads(current_project)
        cp = current_project
        # 判断id是否一致
        new_backers_count = int(response.css('div.new-backers  div.count::text').extract_first())
        existing_backers_count = int(response.css('div.existing-backers  div.count::text').extract_first())
        RewardItem = dict
        # id = Field()
        # rewards = Field()
        # failed_at = Field()  # 如果是成功的项目呢
        # items = Field()
        # updates_count = Field()
        # comments_count = Field()
        # video = Field() # 这个字段是的意义占不清楚
        item = RewardItem()
        item['id'] = cp.get('id', -1)
        item['rewards'] = cp.get('rewards', [])
        item['updates_count'] = cp.get('updates_count')
        item['comments_count'] = cp.get('comments_count')
        item['video'] = cp.get('video')
        yield item
        for k, v in item.iteritems():
            print k, '    :   ', v


class ProfileSpider(scrapy.Spider):
    """
    profile界面的项目和搜索接口的项目数据格式一致，nice！
    """

    name = "stupid_spider1"
    allowed_domains = ["kickstarter.com"]
    start_urls = (
        'https://www.kickstarter.com/profile/hso',
    )

    def parse(self, response):
        projects = response.css('div.react-user-prof-card[data-project] ::attr(data-project)').extract()
        for project in projects:
            data = json.loads(project)
            item = StupidKickstarterItem()
            data = json.loads(data)
            for k, v in data.iteritems():
                item[k] = v
            yield item

        # id = Field()
        # rewards = Field()
        # failed_at = Field()  # 如果是成功的项目呢
        # items = Field()
        # updates_count = Field()
        # comments_count = Field()
        # video = Field() # 这个字段是的意义占不清楚
        # item = RewardItem()
        # item['id'] = cp.get('id', -1)
        # item['rewards'] = cp.get('rewards', [])
        # item['updates_count'] = cp.get('updates_count')
        # item['comments_count'] = cp.get('comments_count')
        # item['video'] = cp.get('video')
        # yield item
        # for k, v in item.iteritems():
        #     print k, '    :   ', v
        #

import scrapy
import cPickle as pickle

class ProfileSpiderSpider(scrapy.Spider):
    name = 'profile_spider1'
    allowed_domains = ['kickstart.com']
    start_urls = ['http://kickstart.com/']


    def parse(self, response):
        usernames = pickle.load(open(r'/home/ubuntu/kickproject/kickstarter/user_name.pkl'))
        profile_url = r'https://www.kickstarter.com/profile/{}'
        for usename in usernames:
            yield scrapy.Request(url=profile_url.format(str(usename)), callback=self.get_project_url)

    def get_project_url(self, response):
        # url_re = 'https://www\.kickstarter\.com/projects.+?/.+?[^/]$'
        # item['url'] = response.css('div.relative.self-start  a.block.img-placeholder.w100p ::attr(href)').extract()
        # item['confirmed'] = True if len(item['url']) == 1 else False
        # item['name'] = response.meta['name']
        # item['user_profile_url'] = response.css('div.relative.self-start a::attr(href)').re(r'.+?(https.+?/profile/.+?)') # list格式
        # return item

        datas = response.css('div.react-user-prof-card ::attr(data-project) ').extract()
        for data in datas:
            item = StupidKickstarterItem()
            data = json.loads(data)
            for k, v in data.iteritems():
                item[k] = v
            yield item