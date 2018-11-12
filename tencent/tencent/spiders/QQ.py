# -*- coding: utf-8 -*-
import scrapy
# 导入链接匹配规则类，用来提取符合规则的链接
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem


class QqSpider(CrawlSpider):
    name = 'QQ'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']
        # response中提取 链接的匹配规则，得出是符合的链接
    pagelink = LinkExtractor(allow=('start=\d+'))
    
    print (pagelink)
    # 可以写多个rule规则
    rules = [
        # follow = True需要跟进的时候加上这句。
        # 有callback的时候就有follow
        # 只要符合匹配规则，在rule中都会发送请求，同是调用回调函数处理响应
        # rule就是批量处理请求
        Rule(pagelink, callback="parse_item", follow=True),
    ]

    # 不能写parse方法，因为源码中已经有了，回覆盖导致程序不能跑

    def parse_item(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 把数据保存在创建的对象中，用字典的形式

            item = TencentItem()
            # 职位
            # each.xpath('./td[1]/a/text()')返回的是列表，extract转为unicode字符串，[0]取第一个
            item['name'] = each.xpath('./td[1]/a/text()').extract()[0]
            # 详情链接
            item['positionlink'] = each.xpath('./td[1]/a/@href').extract()[0]
            # 职位类别
            item['positiontype'] = each.xpath("./td[2]/text()").extract()[0]
            # 人数
            item['peoplenum'] = each.xpath('./td[3]/text()').extract()[0]
            # 工作地点
            item['worklocation'] = each.xpath('./td[4]/text()').extract()[0]
            # 发布时间
            item['publish'] = each.xpath('./td[5]/text()').extract()[0]

            # 把数据交给管道文件
            yield item
