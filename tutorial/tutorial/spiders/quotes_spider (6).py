 #_*_ coding:utf-8 _*_ 

import scrapy

class Quotes_Spider(scrapy.Spider):
	name='quotes6'
	
	start_urls=[
	'http://quotes.toscrape.com/page/1/'
	]
		

	def parse(self,response):
		self.log('Now running %s'%self.name)
		for quote in response.css('div.quote'):
			yield dict(text=quote.css('span.text::text').extract_first(),
						author=quote.css('small.author::text').extract_first(),
						tags=quote.css('div.tags a.tag ::text').extract()
						)
		next_page=response.css('li.next a::attr(href)').extract_first()
		if next_page:
			
			yield response.follow(url=next_page,callback=self.parse)##response.follow 可以传入relative url path

		
		# for a in response.css('li.next a'):
    		# yield response.follow(a, callback=self.parse) ##response.follow也可以直接传入selector xpath 因为response.follow uses their href attribute automatically.

		