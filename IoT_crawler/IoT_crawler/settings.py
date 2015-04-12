# -*- coding: utf-8 -*-

BOT_NAME = 'IoT_crawler'

SPIDER_MODULES = ['IoT_crawler.spiders']
NEWSPIDER_MODULE = 'IoT_crawler.spiders'
ITEM_PIPELINES = {'IoT_crawler.pipelines.MongoPipeline':300}

MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'mydb'
