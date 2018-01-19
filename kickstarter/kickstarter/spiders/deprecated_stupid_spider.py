# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils import engine
from scrapy.exceptions import CloseSpider
# noinspection PyPep8Naming
import cPickle as pickle
from ..items import StupidKickstarterItem
import json
import pymongo
import urllib


client = pymongo.MongoClient()


class StupidSpiderSpider(scrapy.Spider):
    name = "stupid_spider"
    allowed_domains = ["kickstarter.com"]
    # project_keywords = get_keywords_from_csv(r'C:\Users\20189\PyNB\tf_learn\project_name.csv')
    start_urls = (
        'http://www.kickstarter.com/',
    )
    runtime = 60*30  # 爬虫运行一段时间检查是否dead
    pickle_file = r'C:\Users\20189\PyNB\tf_learn\kickstart\name_20k.pkl'
    
    def parse(self, response):
        """
        make Requests for spider to crawler
        :param response: 
        :return: 
        """
        # url = 'https://www.kickstarter.com/discover/advanced?ref=nav_search' \
        #       '&term=The%20Songs%20of%20Adelaide%20%26%20Abullah'
        search_url = 'https://www.kickstarter.com/discover/advanced?ref=nav_search&term={}'
        finished = finished_task(client)
        project_keywords = set()
        for keyword in pickle.load(open(self.pickle_file)):
            if not unicode(keyword, errors='replace') in finished:
                project_keywords.add(keyword)
        print len(project_keywords)
        for i, keyword in enumerate(project_keywords):
            if i > 1600:
                break
            yield scrapy.Request(url=search_url.format(urllib.quote(keyword)), callback=self.get_project_url,
                                 meta={'keyword': keyword})
            # time.sleep(1)
            self.exit_if_spider_dead(timeout=self.runtime)
            # engine.print_engine_status(self.crawler.engine)
            # print 1
        # for keyword in project_keywords:
        #     yield scrapy.Request(url=search_url.format(str(keyword)), callback=self.get_project_url,
        #                               meta={'name': keyword})
        #     yield scrapy.Request(url=search_url.format(str(keyword)), callback=self.get_project_url)

    def get_project_url(self, response):
        """
        parse html and extract items
        :param response: 
        :return: 
        """
        # url_re = 'https://www\.kickstarter\.com/projects.+?/.+?[^/]$'
        # item['url'] = response.css('div.relative.self-start  a.block.img-placeholder.w100p ::attr(href)').extract()
        # item['confirmed'] = True if len(item['url']) == 1 else False
        # item['name'] = response.meta['name']
        # item['user_profile_url'] =
        #            response.css('div.relative.self-start a::attr(href)').re(r'.+?(https.+?/profile/.+?)') # list格式
        # return item
        datas = response.css('div.js-react-proj-card ::attr(data-project) ').extract()
        for data in datas:
            item = StupidKickstarterItem()
            keys = item.field_keys()
            data = json.loads(data)
            for k in data:
                if k in keys:
                    item[k] = data[k]
            yield item
        # time.sleep(10)
        keyword = response.meta.get('keyword')
        task_finished(client, keyword)
        self.exit_if_spider_dead(timeout=self.runtime)
        ''' 翻页
        data_seed = response.css('#projects_list ::attr(data-seed)').extract_first()
        show_more = response.css('div.load_more').extract_first()
        if show_more: # :
            try:
                total_item_num = \
                    response.css('b.count ::text').extract_first().replace(r'\n', '').replace(',', '').split()[0]
                total_item_num = int(total_item_num)
            except:
                total_item_num = 0
            one_page_item_num = 12
            current_page = int(response.meta.get('i', 0))
            next_page = current_page + 1
            if next_page < total_item_num/one_page_item_num:
                load_more_url = r'https://www.kickstarter.com/discover/advanced?google_chrome_workaround&term=load' \
                                r'&woe_id=0&sort=magic&seed={}&page={}'.format(data_seed, next_page)
                yield scrapy.Request(url=load_more_url, callback=self.parse, meta={'i': current_page + 1})
        '''

    def exit_if_spider_dead(self, timeout=60*30):
        """
        if spider runs more than 30min, and no downloader in active,
        then close spider and scrapy exits
        :param timeout: 
        :return: 
        """
        engine_state = engine.get_engine_status(self.crawler.engine)
        run_time = engine_state[0][1]
        active_downloader = engine_state[2][1]
        if run_time > timeout and active_downloader < 1:
            # print run_time
            raise CloseSpider('time runout,used time {}'.format(run_time))


def finished_task(clt):
    # client = pymongo.MongoClient()
    names = set()
    db = 'kickstart'
    collection = 'finished'
    for name in clt[db][collection].find():
        names.add(name['name'])
    return names


def task_finished(clt, keyword):
    # client = pymongo.MongoClient()
    db = 'kickstart'
    collection = 'finished'
    v = unicode(keyword, errors='replace')
    clt[db][collection].update({'name': v}, {'$set': {'name': v}}, upsert=True)
