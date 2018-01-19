# coding=utf-8
# coding:utf-8
import json
import logging
from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from django.core.paginator import Paginator

collection = pymongo.MongoClient('mongodb://kickstart:kickstart@182.254.229.194')['kickstart']['project_data']
logger = logging.getLogger('django')


def getIp(req):
    request = req
    try:
        real_ip = request.META['HTTP_X_FORWARDED_FOR']
        regip = real_ip.split(",")[0]
    except:
        try:
            regip = request.META['REMOTE_ADDR']
        except:
            regip = "1"
    return regip
# Create your views here.

def index(request):
    logger.debug('### IP ###:  {}'.format(getIp(request)))
    limit = 10
    title = "KickStart Project Data"
    successful_count = 132271  # collection.find({'state': 'successful'}).count()
    all_count = collection.count()
    failed_count = 178566  # collection.find({'state': 'failed'}).count()
    live_count = 4135  # collection.find({'state': 'live'}).count()
    items_raw = collection.find({},
                                {'_id': 0, 'urls': 1, 'name': 1, 'photo': 1,  # 'deadline': 1,
                                 'goal': 1, 'state': 1, 'blurb': 1, 'backers_count': 1, 'category': 1,
                                 'creator': 1, 'pledged': 1,
                                 }).skip(2).limit(50)
    items = []
    for item in items_raw:
        items.append({
            'goal': item['goal'],
            'name': item['name'],
            'state': item['state'],
            'backers_count': item['backers_count'],
            'blurb': item['blurb'],
            'photo': item['photo']['med'],
            'pledged': item['pledged'],
            'url': item['urls']['web']['project'],
            'author': item['creator']['name'],
            'category': [item['category']['name'], item['category']['slug']]
        })
    page = request.GET.get('page', 1)
    paginator = Paginator(items, limit)
    loaded = paginator.page(page)
    context = {
        'ItemInfo': loaded,
        'title': title,
        'successful_count': successful_count,
        'all_count': all_count,
        'failed_count': failed_count,
        'live_count': live_count,
        # 'title': title,
    }

    return render(request, 'index_data.html', context)


def about(request):
    logger.debug('### IP ###:  {}'.format(getIp(request)))
    return render(request, 'about.html', {'title': u'关于 KickStarter Spider'})


def docs(request):
    logger.debug('### IP ###:  {}'.format(getIp(request)))
    # f = {'pics': {'$exists': True},
    #      'rewards': {'$exists': True},
    #      'new_backers_count': {'$exists': True}
    #      }
    # data = collection.find_one(f, {'_id': 0})
    # return HttpResponse(json.dumps(data))
    return render(request, 'docs.html', {'title': u'A Record Example'})
