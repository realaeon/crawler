#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
from scrapy.http import Request
from IoT_crawler.items import IoTCrawlerItem,SensorItem


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

class SensorSpider(Spider):
    #log.start("log",loglevel='INFO')
    name = "sensor_crawler"
    allowed_domains = ["www.sensor.com.cn"]
    start_urls = [
            "http://www.sensor.com.cn/product_0_199_0_1.html"
    ]

    def parse(self, response):

        sel = Selector(response)
        sites = sel.xpath('/html/body/div[1]/div[1]/div[7]/div[2]/div[2]/div')
        items = []

        for site in sites:
            item = SensorItem()

            title = site.xpath('./div[2]/div[1]/a/@title').extract()
            picture = site.xpath('./div[1]/a/img/@data-imgfile').extract()
            link = site.xpath('./div[2]/div[1]/a/@href').extract()
            desc = site.xpath('./div[2]/div[2]/div[2]/span/text()').extract()
            producer = site.xpath('./div[2]/p/a/text()').extract()
            prod_area = site.xpath('./div[2]/p/text()').extract()

            item['title'] = [t.encode('utf-8') for t in title]
            item['picture'] = [p.encode('utf-8') for p in picture]
            item['link'] = [l.encode('utf-8') for l in link]
            item['desc'] = [d.encode('utf-8') for d in desc]
            item['producer'] = [p.encode('utf-8') for p in producer]
            item['prod_area'] = [p.encode('utf-8') for p in prod_area]
            yield item
            items.append(item)
            #log.msg("Appending item...",level='INFO')

        urls = sel.xpath('/html/body/div[1]/div[1]/div[7]/div[2]/div[2]/div[8]/div/span[10]/a/@href').extract()
        for url in urls:
            print url
            yield Request(url, callback=self.parse)

