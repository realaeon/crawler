# -*- coding: utf-8 -*-

import scrapy
from scrapy.item import Item,Field

class IoTCrawlerItem(Item):
    title = Field()
    link = Field()
    desc = Field()

