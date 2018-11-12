# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors  import LinkExtractor
from jiumei.items import JiumeiItem
# from items import JiumeiItem

class A99mmSpider(CrawlSpider):
    name = '99mm'
    allowed_domains = ['99mm.me']
    start_urls = ['http://www.99mm.me/qingchun/2833.html']
    linkrule=LinkExtractor(allow=('\w+/\d+\.html'))
    rules=[Rule(linkrule,callback="parse_item",follow=True),]

    def parse_item(self, response):
        item=JiumeiItem()
        item['url']=response.url
        item['Isstr_list']=response.css('script::text').extract()[-1].split('%')
        item['title']=response.css('h2::text').extract_first()

        yield item
        
