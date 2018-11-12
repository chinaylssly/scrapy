# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider,Rule
import scrapy.linkextractors 
from scrapy.selector import Selector
from crawl_spidder.items import CsdnItem



class CsdnSpider(CrawlSpider):
    name = 'CSDN'
    allowed_domains = ['blog.csdn.net']
    download_delay=2
    start_urls=['http://blog.csdn.net/u012150179/article/details/11749017']
    linkext=scrapy.linkextractors.LinkExtractor(allow=('/u\d+/article/details'))
    rules = [Rule(linkext,callback='parse_item',follow=True)]  


    def parse_item(self, response):
        item=CsdnItem()
        blog_url=response.url
        blog_name=response.css('title::text').extract_first().strip()
        item['blog_name']=blog_name
        item['blog_url']=blog_url
        yield item
