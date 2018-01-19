#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : mongo.py
# @Author: Shuaiyy
# @Date  : 2018/1/11 19:35
# @Desc  : move data from many different databases a to b

"""
前期使用该脚本进行数据并库整理，因为此时多个爬虫的数据都是单独存储的，多个数据库中数据有重复，需要去重；
后期增量爬取部分，将使用center cloud database，任务获取和数据提交都在腾讯云上，因此不存在分库存储、数据不一致的问题。
"""

from pymongo import MongoClient
import sys
import  cPickle as pickle
import json

reload(sys)
sys.setdefaultencoding('utf-8')


def get_mongo_client(host='localhost', port=27017, user=None, passwd=None):
    if host and port and user and passwd:
        mongo_url = "mongodb://{}:{}@{}:{}".format(user, passwd, host, port)
        return MongoClient(mongo_url)
    return MongoClient()


def get_id_set(clt, db, collection):
    s = set()
    res = clt[db][collection].find({}, {'_id':0, 'id':1})
    for x in res:
        s.add(x['id'])
    return s

def get_ids_set(collection):
    s = set()
    res = collection.find({}, {'_id':0, 'id':1})
    for x in res:
        s.add(x['id'])
    return s


def insert_from_a_to_b(from_collection, to_collection, ids=set()):
    l = list()
    i = 1
    print len(ids)
    for id in ids:
        data = from_collection.find_one({'id': id}, {'_id': 0})
        if data:
            i += 1
            # print data
            l.append(data)
            if i%100 == 0: print 'read data records {}'.format(i)
        if i%1000 == 0:
            to_collection.insert_many(l)
            print '{} records inserted'.format(i)
            l = list()
    if l:
        to_collection.insert_many(l)
    print '{} records inserted'.format(i)


def test():
    # 源数据库a 腾讯云
    db_a = 'kickstart'
    collection_a = 'project_data'
    # ip = '119.29.16.20' # 我的腾讯云
    # ip = '182.254.229.194' # 钱晨的
    ip = '118.89.35.237' # 菜小鱼的
    user = 'kickstart'
    passwd = 'kickstart'
    # 目标数据库b 本地
    db_b = 'kickstart'
    collection_b = 'project_data'
    # 连接数据库
    client_a = get_mongo_client(host=ip, user=user, passwd=passwd)
    client_b = get_mongo_client()
    # 获取数据集合的id
    ids_a = get_id_set(client_a, db_a, collection_a)
    print 'DB A has {} records'.format(len(ids_a))
    ids_b = get_id_set(client_b, db_b, collection_b)
    print 'DB B has {} records'.format(len(ids_b))
    target_ids = ids_a - ids_b
    print 'A与B的差集大小为{}'.format(len(target_ids))
    # 将a与b的差集数据插入b
    insert_from_a_to_b(client_a[db_a][collection_a], client_b[db_b][collection_b], target_ids)


def test1():
    target_ids = pickle.load(open('target.pkl'))
    print len(target_ids)
    db_a = 'kickstart'
    collection_a = 'project_data'
    db_b = 'newkick'
    collection_b = 'project_data'
    # 连接数据库
    client_a = get_mongo_client()
    # 获取数据集合的id
    print 'A与B的差集大小为{}'.format(len(target_ids))
    # 将a与b的差集数据插入b
    insert_from_a_to_b(client_a[db_a][collection_a], client_a[db_b][collection_b], target_ids)


def move_data():
    collection_a = MongoClient()['kickstart']['project_data']
    collection_b = MongoClient('mongodb://kickwrite:kickstart@182.254.229.194')['kickstart']['project_data']
    id_a = get_ids_set(collection_a)
    print len(id_a)

    id_b = get_ids_set(collection_b)
    print len(id_b)

    target_ids = id_a - id_b
    # 获取数据集合的id
    print 'A与B的差集大小为{}'.format(len(target_ids))
    # 将a与b的差集数据插入b
    insert_from_a_to_b(collection_a, collection_b, target_ids)


if __name__ == '__main__':
    move_data()


