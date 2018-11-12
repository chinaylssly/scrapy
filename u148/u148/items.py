# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class U148Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    link=scrapy.Field()
    # author=scrapy.Field()
    # author_link=scrapy.Field()
    # tag=scrapy.Field()
    # category=scrapy.Field()
    content=scrapy.Field()
