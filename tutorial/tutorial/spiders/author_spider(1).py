 #_*_ coding:utf-8 _*_ 

import scrapy

class Author_Spider(scrapy.Spider):
	name='author1'
	start_urls=['http://quotes.toscrape.com/']
		

	def parse(self,response):
		self.log('Now running %s'%self.name)

		for quote in response.css('div.quote'):
			yield dict(text=quote.css('span.text::text').extract_first(),
						author=quote.css('small.author::text').extract_first(),
						tags=quote.css('div.tags a.tag ::text').extract()
						)

		#解析作者详情页
		for href in response.css('.author + a::attr(href)'):
			yield response.follow(url=href,callback=self.parse_author)

		#解析下一页
		for href in response.css('li.next a::attr(href)'):
			yield response.follow(url=href,callback=self.parse)

	def parse_author(self,response):

		def extract_by_css(query):
			return response.css(query).extract_first().strip()

		yield {
		'name':extract_by_css('h3.author-title::text'),
		'birthday':extract_by_css('.author-born-date::text'),
		'bio':extract_by_css('.author-description::text'),
		}
	