# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位
    name = scrapy.Field()
    # 详情链接
    positionlink = scrapy.Field()
    #职位类别
    positiontype = scrapy.Field()
    # 人数
    peoplenum = scrapy.Field()
    # 工作地点
    worklocation = scrapy.Field()
    # 发布时间
    publish = scrapy.Field()

