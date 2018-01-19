#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : kickurls.py
# @Author: Shuaiyy
# @Date  : 2018/1/14 16:49
# @Desc  : 

explore_urls = [
    ('https://www.kickstarter.com/discover/advanced?woe_id=0&staff_picks=1&sort=magic&seed=2526477&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&sort=popularity&seed=2526478&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&sort=newest&seed=2526479&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?woe_id=0&staff_picks=1&sort=newest&seed=2526478&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?woe_id=0&staff_picks=1&sort=newest&seed=2526527&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&sort=end_date&seed=2526479&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&sort=most_funded&seed=2526540&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&sort=most_backed&seed=2526540&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?woe_id=0&sort=popularity&seed=2526480&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?woe_id=0&staff_picks=1&raised=1&sort=end_date&seed=2526482&page={}',
     33),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=0&sort=end_date&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=0&sort=magic&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=0&sort=popularity&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=0&sort=newest&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=0&sort=most_funded&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=0&sort=most_backed&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=2&sort=end_date&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=2&sort=magic&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=2&sort=popularity&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=2&sort=newest&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=2&sort=most_funded&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&raised=2&sort=most_backed&seed=2526482&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?staff_picks=1&sort=end_date&seed=2526541&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?sort=popularity&seed=2526528&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?woe_id=0&sort=magic&seed=2526528&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?sort=newest&seed=2526528&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?sort=end_date&seed=2526528&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?sort=most_funded&seed=2526528&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?sort=most_backed&seed=2526528&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&sort=popularity&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&sort=most_funded&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&sort=most_backed&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&sort=popularity&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&sort=most_funded&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&sort=most_backed&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&sort=popularity&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&sort=most_funded&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&sort=most_backed&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&sort=popularity&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&sort=most_funded&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&sort=most_backed&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=4&sort=magic&seed=2526544&page={}', 23),
    ('https://www.kickstarter.com/discover/advanced?pledged=4&sort=popularity&seed=2526544&page={}', 23),
    ('https://www.kickstarter.com/discover/advanced?pledged=4&sort=newest&seed=2526544&page={}', 23),
    ('https://www.kickstarter.com/discover/advanced?pledged=4&sort=end_date&seed=2526544&page={}', 23),
    ('https://www.kickstarter.com/discover/advanced?pledged=4&sort=most_funded&seed=2526544&page={}', 23),
    ('https://www.kickstarter.com/discover/advanced?pledged=4&sort=most_backed&seed=2526544&page={}', 23),
    ('https://www.kickstarter.com/discover/advanced?goal=0&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=0&sort=popularity&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=0&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=0&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=0&sort=most_funded&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=0&sort=most_backed&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=1&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=1&sort=popularity&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=1&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=1&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=1&sort=most_funded&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=1&sort=most_backed&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=2&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=2&sort=popularity&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=2&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=2&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=2&sort=most_funded&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=2&sort=most_backed&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=3&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=3&sort=popularity&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=3&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=3&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=3&sort=most_funded&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=3&sort=most_backed&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?goal=4&sort=magic&seed=2526544&page={}', 117),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=0&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=0&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=0&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=0&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=0&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=0&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=1&sort=magic&seed=2526544&page={}', 198),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=2&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=2&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=2&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=2&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=2&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=0&raised=2&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=1&raised=0&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=1&raised=0&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=1&raised=0&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=1&raised=0&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=1&raised=0&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=1&raised=0&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?woe_id=0&pledged=0&goal=1&raised=1&sort=magic&seed=2526544&page={}',
     33),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=1&raised=2&sort=magic&seed=2526544&page={}', 27),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=2&raised=0&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=2&raised=0&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=2&raised=0&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=2&raised=0&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=2&raised=0&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=2&raised=0&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=3&raised=0&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=3&raised=0&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=3&raised=0&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=3&raised=0&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=3&raised=0&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=3&raised=0&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=0&goal=4&raised=0&sort=magic&seed=2526544&page={}', 99),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=0&raised=1&sort=magic&seed=2526544&page={}', 26),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=0&raised=2&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=0&raised=2&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=0&raised=2&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=0&raised=2&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=0&raised=2&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=0&raised=2&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=0&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=0&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=0&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=0&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=0&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=0&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=1&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=1&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=1&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=1&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=1&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=1&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=2&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=2&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=2&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=2&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=2&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=1&raised=2&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=2&raised=0&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=2&raised=0&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=2&raised=0&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=2&raised=0&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=2&raised=0&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=2&raised=0&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=2&raised=1&sort=magic&seed=2526544&page={}', 18),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=2&raised=2&sort=magic&seed=2526544&page={}', 6),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=3&raised=0&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=3&raised=0&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=3&raised=0&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=3&raised=0&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=3&raised=0&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=3&raised=0&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=1&goal=4&raised=0&sort=magic&seed=2526544&page={}', 10),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=0&raised=2&sort=magic&seed=2526544&page={}', 52),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=1&raised=1&sort=magic&seed=2526544&page={}', 5),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=1&raised=2&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=1&raised=2&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=1&raised=2&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=1&raised=2&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=1&raised=2&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=1&raised=2&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=0&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=0&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=0&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=0&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=0&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=0&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=1&sort=magic&seed=2526544&page={}', 64),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=2&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=2&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=2&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=2&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=2&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=2&raised=2&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=3&raised=0&sort=magic&seed=2526544&page={}', 145),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=3&raised=1&sort=magic&seed=2526544&page={}', 2),
    ('https://www.kickstarter.com/discover/advanced?pledged=2&goal=4&raised=0&sort=magic&seed=2526544&page={}', 6),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=0&raised=2&sort=magic&seed=2526544&page={}', 2),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=1&raised=2&sort=magic&seed=2526544&page={}', 43),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=2&raised=2&sort=magic&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=2&raised=2&sort=popularity&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=2&raised=2&sort=newest&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=2&raised=2&sort=end_date&seed=2526544&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=2&raised=2&sort=most_funded&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=2&raised=2&sort=most_backed&seed=2526544&page={}',
     200),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=3&raised=0&sort=magic&seed=2526544&page={}', 11),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=3&raised=1&sort=magic&seed=2526544&page={}', 2),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=3&raised=2&sort=magic&seed=2526544&page={}', 96),
    ('https://www.kickstarter.com/discover/advanced?pledged=3&goal=4&raised=0&sort=magic&seed=2526544&page={}', 2),
    ('https://www.kickstarter.com/discover/advanced?pledged=4&goal=1&raised=2&sort=magic&seed=2526544&page={}', 1),
    ('https://www.kickstarter.com/discover/advanced?pledged=4&goal=2&raised=2&sort=magic&seed=2526544&page={}', 17),
    ('https://www.kickstarter.com/discover/advanced?pledged=4&goal=3&raised=2&sort=magic&seed=2526544&page={}', 11),
    ('https://www.kickstarter.com/discover/advanced?pledged=4&goal=4&raised=2&sort=magic&seed=2526544&page={}', 2),
    ('https://www.kickstarter.com/discover/advanced?category_id=1&woe_id=0&sort=magic&seed=2526529&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=1&sort=popularity&seed=2526529&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=1&sort=newest&seed=2526529&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=1&sort=end_date&seed=2526529&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=1&sort=most_funded&seed=2526529&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=1&sort=most_backed&seed=2526529&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=3&woe_id=0&sort=magic&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=3&sort=popularity&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=3&sort=newest&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=3&sort=end_date&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=3&sort=most_funded&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=3&sort=most_backed&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=26&woe_id=0&sort=magic&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=26&sort=popularity&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=26&sort=newest&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=26&sort=end_date&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=26&sort=most_funded&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=26&sort=most_backed&seed=2526530&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=6&woe_id=0&sort=magic&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=6&sort=popularity&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=6&sort=newest&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=6&sort=end_date&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=6&sort=most_funded&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=6&sort=most_backed&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=7&woe_id=0&sort=magic&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=7&sort=popularity&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=7&sort=newest&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=7&sort=end_date&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=7&sort=most_funded&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=7&sort=most_backed&seed=2526531&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=9&woe_id=0&sort=magic&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=9&sort=popularity&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=9&sort=newest&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=9&sort=end_date&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=9&sort=most_funded&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=9&sort=most_backed&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=11&woe_id=0&sort=magic&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=11&sort=popularity&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=11&sort=newest&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=11&sort=end_date&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=11&sort=most_funded&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=11&sort=most_backed&seed=2526532&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=10&woe_id=0&sort=magic&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=10&sort=popularity&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=10&sort=newest&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=10&sort=end_date&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=10&sort=most_funded&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=10&sort=most_backed&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=12&woe_id=0&sort=magic&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=12&sort=popularity&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=12&sort=newest&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=12&sort=end_date&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=12&sort=most_funded&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=12&sort=most_backed&seed=2526533&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=13&woe_id=0&sort=magic&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=13&sort=popularity&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=13&sort=newest&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=13&sort=end_date&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=13&sort=most_funded&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=13&sort=most_backed&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=14&woe_id=0&sort=magic&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=14&sort=popularity&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=14&sort=newest&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=14&sort=end_date&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=14&sort=most_funded&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=14&sort=most_backed&seed=2526534&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=15&woe_id=0&sort=magic&seed=2526536&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=15&sort=popularity&seed=2526536&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=15&sort=newest&seed=2526536&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=15&sort=end_date&seed=2526536&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=15&sort=most_funded&seed=2526536&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=15&sort=most_backed&seed=2526536&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=18&woe_id=0&sort=magic&seed=2526537&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=18&sort=popularity&seed=2526537&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=18&sort=newest&seed=2526537&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=18&sort=end_date&seed=2526537&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=18&sort=most_funded&seed=2526537&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=18&sort=most_backed&seed=2526537&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=16&woe_id=0&sort=magic&seed=2526538&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=16&sort=popularity&seed=2526538&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=16&sort=newest&seed=2526538&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=16&sort=end_date&seed=2526538&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=16&sort=most_funded&seed=2526538&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=16&sort=most_backed&seed=2526538&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=17&woe_id=0&sort=magic&seed=2526539&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=17&sort=popularity&seed=2526539&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=17&sort=newest&seed=2526539&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=17&sort=end_date&seed=2526539&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=17&sort=most_funded&seed=2526539&page={}', 200),
    ('https://www.kickstarter.com/discover/advanced?category_id=17&sort=most_backed&seed=2526539&page={}', 200)
]


def make_urls():
    """
    产生52078个请求，能够爬到819510个item，不重复的大概2w左右。
    :return: 
    """
    urls = []
    for url, maxpage in explore_urls:
        for page in range(1, maxpage):
            urls.append(url.format(page))
    return urls


def make_urls_for_new():
    """
    产生1710个请求，定期抓最新的项目信息
    :return: 
    """
    urls = []
    for url, maxpage in explore_urls:
        if ('end_date' in url) or ('newest' in url):
            maxpage = maxpage if maxpage < 20 else 20
            for page in range(1, maxpage):
                urls.append(url.format(page))
    return urls


if __name__ == '__main__':
    pass
    # x = 0
    # for url, maxpage in explore_urls:
    #     x += maxpage - 1
    # print x  # 52078
    # x = 0
    # for url, maxpage in explore_urls:
    #     if 'end_date' in url or 'newest' in url:
    #         maxpage = maxpage if maxpage < 20 else 20
    #         x += maxpage - 1
    # print x  # 1710
