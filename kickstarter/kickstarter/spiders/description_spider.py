# -*- coding: utf-8 -*-
import scrapy
from ..util.mongo import MongoOperate
from ..items import DescriptionItem


class DescriptionSpiderSpider(scrapy.Spider):
    name = "description_spider"
    allowed_domains = ["kickstarter.com"]
    start_urls = (
        'https://www.kickstarter.com/',
        # 'https://www.kickstarter.com/projects/952823766/electro-pop-band-nans-and-nat-make-their-debut-alb'
    )

    def parse(self, response):
        task = MongoOperate().get_description_task()
        for id, url in task:
            yield scrapy.Request(url=url, callback=self.parse_description, meta={'id': id})

    def parse_description(self, response):
        item = DescriptionItem()
        item['id'] = response.meta.get('id', -1)
        item['pics'] = response.css(".full-description figure img::attr(src)").extract()
        item['pic_count'] = len(item['pics'])
        item['gif_count'] = len([x for x in item['pics'] if '.gif' in x])
        item['hyperlink'] = response.css('.full-description a::attr(href)').extract()
        item['hyperlink_count'] = len(set(item['hyperlink']))
        yield item
