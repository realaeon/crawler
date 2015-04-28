# -*- coding: utf-8 -*-

BOT_NAME = 'IoT_crawler'

DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

SPIDER_MODULES = ['IoT_crawler.spiders']
NEWSPIDER_MODULE = 'IoT_crawler.spiders'
ITEM_PIPELINES = {'IoT_crawler.pipelines.MongoPipeline':300}
#ITEM_PIPELINES = {'IoT_crawler.pipelines.IoTPipeline':300}

MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'mydb'
