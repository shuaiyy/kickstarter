# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field
from kickstarter.util.mongo import MongoOperate

mo = MongoOperate()
collection = mo.get_writeable_collection()


class StupidKickstarterItem(Item):
    disable_communication = Field()
    current_currency = Field()
    photo = Field()
    currency = Field()
    deadline = Field()
    currency_trailing_code = Field()
    id = Field()
    state_changed_at = Field()
    category = Field()
    goal = Field()
    staff_pick = Field()
    pledged = Field()
    creator = Field()
    usd_type = Field()
    state = Field()
    static_usd_rate = Field()
    location = Field()
    launched_at = Field()
    blurb = Field()
    profile = Field()
    fx_rate = Field()
    urls = Field()
    usd_pledged = Field()
    percent_funded = Field()
    converted_pledged_amount = Field()
    slug = Field()
    name = Field()
    country = Field()
    created_at = Field()
    backers_count = Field()
    currency_symbol = Field()
    spotlight = Field()
    is_starrable = Field()
    def insert_to_mongodb(self):
        # db = client['kickstart']
        # collection = db['project_data']
        # 如果存在则更新，不存在则插入
        collection.update_one({'id': self['id']}, {'$set': dict(self)}, upsert=True)

    def field_keys(self):
        return self.fields.keys()
        # 啊啊啊，我傻了！
        # return item.fields.keys()
        # return ['is_starrable', 'spotlight', 'currency_symbol', 'backers_count', 'created_at',
        #         'country', 'name', 'slug','converted_pledged_amount', 'percent_funded',
        #         'usd_pledged', 'urls', 'fx_rate', 'profile', 'blurb',
        #         'launched_at', 'location', 'static_usd_rate', 'state', 'usd_type',
        #         'creator', 'pledged', 'staff_pick', 'goal', 'category',
        #         'state_changed_at', 'id', 'currency_trailing_code', 'deadline', 'currency',
        #         'photo', 'current_currency', 'disable_communication'
        #         ]


class RewardItem(Item):
    id = Field()
    rewards = Field()
    rewards_level = Field()
    comments_count = Field()
    updates_count = Field()
    video = Field()
    is_first_creator = Field()

    def insert_to_mongodb(self):
        collection.update_one({'id': self['id']}, {'$set': dict(self)})


class CommunityItem(Item):
    id = Field()
    new_backers_count = Field()
    return_backers_count = Field()

    def insert_to_mongodb(self):
        collection.update_one({'id': self['id']}, {'$set': dict(self)})
        pass


class DescriptionItem(Item):
    id = Field()
    pics = Field()
    pic_count = Field()
    gif_count = Field()
    # is_new_creator = Field()
    hyperlink = Field()
    hyperlink_count = Field()
    # has_video = Field()

    def insert_to_mongodb(self):
        collection.update_one({'id': self['id']}, {'$set': dict(self)})
        pass

class OutdateItem(Item):
    deadline = Field()
    id = Field()
    state_changed_at = Field()
    goal = Field()
    pledged = Field()
    state = Field()
    converted_pledged_amount = Field()
    backers_count = Field()


    def insert_to_mongodb(self):
        # db = client['kickstart']
        # collection = db['project_data']
        # 如果存在则更新，不存在则插入
        collection.update_one({'id': self['id']}, {'$set': dict(self)}, upsert=True)

# # 不用这个啦，按照kickstarter的命名风格设置字段
# class KickstarterItem(Item):
#     # define the fields for your item here like:
#     title = scrapy.Field()  # 项目名称
#     blurb = scrapy.Field()  # 项目简介
#     funder_name = scrapy.Field() # 创建者
#     funder_id = scrapy.Field() # 用户id
#     location = scrapy.Field()
#     category = scrapy.Field()
#     deadline = scrapy.Field()
#     pledged = scrapy.Field() # 实际筹集资金
#     goal = scrapy.Field()    # 筹资目标
#     funded_percentage = scrapy.Field() # 筹资百分比，如果项目成功的，则应该也可以由pledged和goal计算出。
#     backed_num = scrapy.Field() # 支持人数
#     comment_num = scrapy.Field() # 评论数
#     ask_num = scrapy.Field()  # 提问数量
#     updates_num = scrapy.Field() # 项目更新次数
#     new_backers_num = scrapy.Field() # 新人数，第一次投资
#     old_backers_num = scrapy.Field() # 老人 = 总的-新人？
#     support_level_backers = scrapy.Field() # 不同等级资助的人数，($5: 100backers) {'5'：100}
#     support_currency = scrapy.Field()  # 美元还是其他货币种类
#     #support_level_num = scrapy.Field() # support_level的长度
#
#     url = scrapy.Field()  # 项目所在的url
#     html = scrapy.Field() # 项目描述部分的HTML代码
#     text = scrapy.Field() # 项目描述文本，由html去除样式得到
#     pic_num = scrapy.Field()  # 项目描述中的pic
#     hyperlink_num = scrapy.Field() #
#     is_new_creator = scrapy.Field()
#     has_video = scrapy.Field()
#     state = scrapy.Field()  # 成功，失败，进行中
#
#     def insert_to_mongodb(self):
#         # db=
#         # collection =
#         pass

if __name__ == '__main__':
    item = StupidKickstarterItem()
    # print dir(item)
    # print item.keys()
    print item.fields.keys()
    print len(item.fields.keys())