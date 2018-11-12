# -*- coding: utf-8 -*-
import scrapy
# from umei.items import UmeiItem
from items import UmeiItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class A99mmSpider(scrapy.Spider):
    name = '99mm'
    allowed_domains = ['99mm.me']
    start_urls = ['http://99mm.me/']


    def parse(self,response):



    	ul=response.css('#piclist')[0]
    	links=ul.css('dd a::attr(href)')
    	for link in links:
    		yield response.follow(link,callback=self.parse_item)

    	next=response.css('.next::attr(href)').extract_first()

    	yield response.follow(next,callback=self.parse)
	



    def parse_item(self, response):

    	item=UmeiItem()
    	item['url']=response.url
    	item['title']=response.css('h2::text').extract_first()
    	raw_str=response.css('script::text').extract()[-1]

    	item['Isstr']=raw_str
    	l=raw_str.split(',')
    	host='http://img.99mm.net/'
    	pages=l[2]
    	year=l[4]
    	index=l[5]
    	item['img_info']=dict(host=host,yaer=year,index=index,pages=pages)  ##img_url形式：host/year/index/extend

    	yield item

        
if __name__ =='__main__':
    process=CrawlerProcess(get_project_settings())
    process.crawl('99mm')
    process.start()
