# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from u148.items import U148Item


class U148NetSpider(CrawlSpider):
    name = 'u148.net'
    allowed_domains = ['u148.net']
    start_urls = ['http://www.u148.net/']
    linkrule=LinkExtractor(allow=('article/\d+'))
    rules=[Rule(linkrule,callback='parse_item',follow=True)]

    def parse_item(self, response):
    	def extract_by_css(query):
    		result=response.css(query).extract_first()
    		if not result:
    			return None
    		else:
    			return result.strip()

    	item=U148Item()
    	item['link']=response.url
    	item['title']=extract_by_css('.content h1 a::text')
    	item['content']=response.css('.contents p::text').extract()
    	yield item
    	# item['link']=response.css('.content h1 a::attr(href)')
    	# item['author']=extract_by_css('.article-info  a:nth-child(3)::text')
    	# item['author_link']=response.css('.article-info  a:nth-child(3)::attr(href)')
		# item['category']=
		# item['tag']=






    
