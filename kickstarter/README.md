[TOC]

## KickStarter Spiders  With Scrapy

this project scrapes [kickstarter.com](kickstarter.com) ，to collect info  of  Crowd-funding  projects founded in kickstarter website。

take risk on your own when  use spiders on Kickstarter or any other websites.

if this  project helped you, please give it a star, thanks ;)

### Data Record

i have scraped more than 350k records, which 4GB disk space used. 

here are some fields that  may be useful,

 `name`   `blurb`   `category`   `rewards`   `video`  `pic_count`  `hyperlink_count` 

 `is_first_creator`

`goal`   `pledged`    `deadline`  `state`   `backers_count` `comments_count`  `updates_count` 

all fields can be seen in `items.py`.

![mark](http://o8i01ajlj.bkt.clouddn.com/blog/180114/5JkHH6A24G.jpg?imageslim)



### Spider list

+ new_project_spider

  find project from index or search page,then save item to mongodb.

+ community_spider

  update records in mongodb, add  some  fields which value are collected from project community page.

+ description_spider

  update records in mongodb, add  some  fields which value are collected from project desription page.

+ live_outdate_spider

  update projects in mongodb which marked state as "live", but actually Expiration of the deadline.

+ profile_spider

  it's  a  `# TODO` plan.  to get project item from users'  profile index page

+ reward_spider

  update projects in mongodb and add rewards info.

+ stupid_spider

  this is stupid.

### Project environment

+ mongodb  **X64**

  to accelerate access speed, **build index** on the filed of `id`.

  if you use 32-bit mongodb, the db data size has a limit of 2GB, which can only store 100k records in my test.

  if use remote mongodb，create two user of  `read` and `readWrite`  in admin for db `kickstart`

+ python 2.7

+ scrapy 1.1 or higher

+ pymongo

If you don't have scrapy running environment, see it's website to get a start.





### How to use

before runing,  check `settings.py`

```python

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Accept-Language': 'en',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

# Configure item pipelines
ITEM_PIPELINES = {
   'kickstarter.pipelines.MongodbPipeline': 300,
}

# LOG_LEVEL = 'INFO' #'DEBUG'
LOG_LEVEL = 'DEBUG'
LOG_FILE = "KickSpider.log"

# mongodb user and  password
# localhost with no auth
MONGO_READ = None # 'mongodb://kickstart:kickstart@182.254.229.194'
MONGO_WRITE = None #  'mongodb://kickwrite:kickstart@182.254.229.194'
# remote mongodb uri with user of "read" and "readWrite".
# MONGO_READ = 'mongodb://user_read:pass@182.254.229.194'
# MONGO_WRITE = 'mongodb://use_readwrite:pass@182.254.229.194'
DBNAME = 'kickstart'
COLLECTION = 'project_data'
SKIP_NUM = 1000
LIMIT_NUM = 100
```

after that, run `python run_spider.py` and enjoy :)



