# _*_ coding:utf-8 _*_ 

import scrapy

class Quotes_Spider(scrapy.Spider):
	name='quotes4'
	def start_requests(self):
		urls=[
		'http://quotes.toscrape.com/page/1/',
		'http://quotes.toscrape.com/page/2/',
		]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):
		self.log('Now running %s'%self.name)
		for quote in response.css('div.quote'):
			yield dict(text=quote.css('span.text::text').extract_first(),
						author=quote.css('small.author::text').extract_first(),
						tags=quote.css('div.tags a.tag ::text').extract()
						)

		