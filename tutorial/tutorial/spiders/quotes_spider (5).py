 #_*_ coding:utf-8 _*_ 

import scrapy

class Quotes_Spider(scrapy.Spider):
	name='quotes5'
	
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
			next_page=response.urljoin(next_page) ##下一页的url，继承于urlparse.urljoin(response.url,url)

			yield scrapy.Request(url=next_page,callback=self.parse)