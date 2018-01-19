#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : urls.py
# @Author: Shuaiyy
# @Date  : 2018/1/14 20:30
# @Desc  : 

from django.conf.urls import include, url
from django.contrib import admin
from views import index, about, docs

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^about/', about, name='about'),
    url(r'^docs/', docs, name='docs'),
]


