#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log

from IoT_crawler.items import IoTCrawlerItem


class W3schoolSpider(Spider):
    #log.start("log",loglevel='INFO')
    name = "IoT_crawler"
    allowed_domains = ["http://www.sensor.com.cn/"]
    start_urls = [
            "http://www.sensor.com.cn/"
    ]

    def parse(self, response):

        sel = Selector(response)
        sites = sel.xpath('/html/body/div[1]/div[1]/div[6]/div[8]/div[2]//dd/a')
        items = []

        for site in sites:
            item = IoTCrawlerItem()

            title = site.xpath('./text()').extract()
            link = site.xpath('./@href').extract()
            desc = site.xpath('./@title').extract()

            item['title'] = [t.encode('utf-8') for t in title]
            item['link'] = [l.encode('utf-8') for l in link]
            item['desc'] = [d.encode('utf-8') for d in desc]
            items.append(item)

            log.msg("Appending item...",level='INFO')


        log.msg("Append done.",level='INFO')
        return items

