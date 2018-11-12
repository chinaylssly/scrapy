# -*- coding: utf-8 -*-
import scrapy


class KrSpider(scrapy.Spider):
    name = 'kr'
    allowed_domains = ['hanfan.cc']
    start_urls = ['http://hanfan.cc/']

    def parse(self, response):
        pass
