 #_*_ coding:utf-8 _*_ 

import scrapy

#通过getattr传入tag参数，构建类似于 http://quotes.toscrape.com/tag/humor形式的url
class Author_Spider(scrapy.Spider):
	name='tag'
	def start_requests(self):
		url='http://quotes.toscrape.com/'
		tag=getattr(self,'tag',None)
		if tag:
			url=url+'tag/'+tag
		yield scrapy.Request(url=url,callback=self.parse)
		

	def parse(self,response):
		self.log('Now running %s'%self.name)

		for quote in response.css('div.quote'):
			yield dict(text=quote.css('span.text::text').extract_first(),
						author=quote.css('small.author::text').extract_first(),
						)

		#解析下一页
		for href in response.css('li.next a::attr(href)'):
			yield response.follow(url=href,callback=self.parse)

	