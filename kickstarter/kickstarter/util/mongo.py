#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : mongo.py
# @Author: Shuaiyy
# @Date  : 2018/1/12 19:41
# @Desc  : 
from pymongo import MongoClient
# from ..settings import *
from kickstarter.settings import *
import time
import sys

reload(sys)
# noinspection PyUnresolvedReferences
sys.setdefaultencoding('utf-8')


class MongoOperate(object):
    client_read = None
    client_write = None

    def __init__(self):
        self.client_read = MongoClient(MONGO_READ)
        self.client_write = MongoClient(MONGO_WRITE)

    def get_readable_collection(self):
        return self.client_read[DBNAME][COLLECTION]

    def get_writeable_collection(self):
        return self.client_write[DBNAME][COLLECTION]

    def get_rewards_task(self):
        client = self.get_readable_collection()
        reward_urls = []
        records = client.find({'rewards': {'$exists': False}}, {'urls': 1, '_id': 0}).skip(SKIP_NUM).limit(LIMIT_NUM)
        for record in records:
            # noinspection PyBroadException
            try:
                reward_url = record.get('urls').get('web').get('rewards')
                reward_urls.append(reward_url)
            except:
                reward_url = record.get('urls').get('web').get('project') + '/rewards'
                reward_urls.append(reward_url)
        return reward_urls

    def get_community_task(self):
        # 'https://www.kickstarter.com/projects/952823766/electro-pop-band-nans-and-nat-make-their-debut-alb/community'
        client = self.get_readable_collection()
        community_urls = []
        # 只有成功的项目有 'state': {'$ne': 'live'},支持者大于10
        records = client.find({'new_backers_count': {'$exists': False},
                               'state': 'successful',
                               'backers_count': {'$gt': 10}, },
                              {'urls': 1, '_id': 0, 'id': 1}).skip(SKIP_NUM).limit(LIMIT_NUM)
        for record in records:
            # noinspection PyBroadException
            try:
                community_url = record.get('urls').get('web').get('project') + '/community'
                id = record.get('id')
                community_urls.append((id, community_url))
            except:
                pass
        return community_urls

    def get_description_task(self):
        # 'https://www.kickstarter.com/projects/277670373/pre-orders-for-the-chimera-of-prague-a-romantic-no/description'
        client = self.get_readable_collection()
        description_urls = []
        records = client.find({'pic_count': {'$exists': False}, 'state': {'$ne': 'live'}},
                              {'urls': 1, 'id': 1, '_id': 0}).skip(SKIP_NUM).limit(LIMIT_NUM)
        for record in records:
            # noinspection PyBroadException
            try:
                project_url = record.get('urls').get('web').get('project') + '/description'
                id = record.get('id')
                description_urls.append((id, project_url))
            except:
                pass
        return description_urls

    def get_outdate_task(self):
        # TODO  更新已经过期但数据库中仍标记为Live的project
        # 'https://www.kickstarter.com/projects/277670373/pre-orders-for-the-chimera-of-prague-a-romantic-no/description'
        now = int(time.time())  # 时间戳取整
        client = self.get_readable_collection()
        outdate_urls = []
        records = client.find({'pic_count': {'$exists': False}, 'state': 'live', 'deadline': {'$lt': now}
                               }, {'urls': 1, '_id': 0}).limit(LIMIT_NUM)
        for record in records:
            # noinspection PyBroadException
            try:
                project_url = record.get('urls').get('web').get('project')
                outdate_urls.append(project_url)
            except:
                pass
        return outdate_urls

    def get_users(self):
        """
        返回数据库已有的用户
        :return: 
        """
        client = self.get_readable_collection()
        records = client.find({}, {'_id': 0, 'urls': 1})
        usernames = set()
        for record in records:
            # noinspection PyBroadException
            try:
                project_url = record.get('urls').get('web').get('project')
                usernames.add(project_url.split('projects/')[-1].split('/')[0])
            except:
                pass
        return usernames


if __name__ == '__main__':
    mongo = MongoOperate()
    xxx = mongo.get_community_task()
    print len(xxx)
    # for x in xxx:
    #     print x
        # print y
        # break
    # c2 = MongoClient(MONGO_WRITE)
    # print c2[DBNAME][COLLECTION].count()
