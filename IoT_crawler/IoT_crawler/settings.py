# -*- coding: utf-8 -*-

BOT_NAME = 'IoT_crawler'

DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

SPIDER_MODULES = ['IoT_crawler.spiders']
NEWSPIDER_MODULE = 'IoT_crawler.spiders'
ITEM_PIPELINES = {#'IoT_crawler.pipelines.MongoPipeline':300,
                  'IoT_crawler.pipelines.JsonPipeline':200,}

####mongodb##### 
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'mydb'

####redis####
REDIS_URL = None
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
SCHEDULER = "IoT_crawler.scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = "IoT_crawler.scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "IoT_crawler.scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "IoT_crawler.scrapy_redis.queue.SpiderStack"
