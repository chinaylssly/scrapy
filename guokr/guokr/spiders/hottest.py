# -*- coding: utf-8 -*-
import scrapy


class HottestSpider(scrapy.Spider):
    name = 'hottest'
    allowed_domains = ['guokr.com']
    start_urls = ['http://guokr.com/']

    def parse(self, response):
        pass
