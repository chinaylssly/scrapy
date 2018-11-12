# _*_ coding:utf-8 _*_ 

import scrapy

class Quotes_Spider(scrapy.Spider):
	name='quotes'
	def start_requests(self):
		urls=[
		'http://quotes.toscrape.com/page/1/',
		'http://quotes.toscrape.com/page/2/',
		]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):
		page=response.url.split('/')[-2]
		filename='quotes-%s-%s.html'%(page,self.name)
		with open(filename,'wb')as f:
			f.write(response.body)
		self.log('Save file %s runing in %s'%(filename,self.name))