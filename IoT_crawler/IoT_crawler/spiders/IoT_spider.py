#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from IoT_crawler.scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from scrapy import log
from scrapy.http import Request,FormRequest
from IoT_crawler.items import IoTCrawlerItem,SensorItem


class IoTSpider(RedisSpider):
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
    name = "sensor_crawler"
    allowed_domains = ["www.sensor.com.cn"]
    start_urls = [
        "http://www.sensor.com.cn/product_0_206_0_1.html"
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

        urls = sel.xpath('/html/body/div[1]/div[1]/div[7]/div[2]/div[2]/div[8]/div/span[10]/a/@href').extract()
        for url in urls:
            print url
            yield Request(url, callback=self.parse)

            
class Alibaba(Spider):
    name = "baba_crawler"
    myKeywords = '%C0%B6%D1%C0%C4%A3%BF%E9'#'zigbee%C4%A3%BF%E9'  #'wifi%C4%A3%BF%E9'
    download_delay = 1
    start_urls = []
    for i in range(1,3):
        start_urls.append("http://s.1688.com/selloffer/offer_search.htm?keywords="+myKeywords+"#beginPage="+str(i))

    '''
    def start_requests(self):
        return [Request("http://login.1688.com/",callback=self.logged_in)]
    def logged_in(self,response):
        print 'Preparing login'
        return [FormRequest.from_response(response,#"http://www.zhihu.com/login",
                                          formdata = {'TPL_username': '','TPL_password': '','rememberme': 'y'},
                                          callback = self.parse
                                        )]
    '''

    def parse(self,response):
        sel = Selector(response)
        items = []
        
        for i in range(1,21):
            offerID = 'offer'+ str(i)
            site = sel.xpath("//*[@id=\'" + offerID + '\']')
            item = SensorItem()

            title = site.xpath("./div[2]/a[1]/@title").extract()
            picture = site.xpath("./div[1]/div[1]/a/img/@src").extract()
            producer = site.xpath('./div[3]/a/text()').extract()
            prod_area = site.xpath('./div[4]/div[1]/text()').extract()
            price = site.xpath('./div[1]/div[2]/span[1]/text()').extract()
            link = site.xpath('./div[2]/a[1]/@href').extract()
            item['link'] = [l.encode('utf-8') for l in link]
            item['price'] = [p.encode('utf-8') for p in price]
            item['prod_area'] = [p.encode('utf-8') for p in prod_area]
            item['producer'] = [p.encode('utf-8') for p in producer]
            item['picture'] = [p.encode('utf-8') for p in picture]
            item['title'] = [t.encode('utf-8') for t in title]
            yield item

     
