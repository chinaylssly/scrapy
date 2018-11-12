# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from collections import OrderedDict

class MafengwoPipeline(object):

    def __init__(self):

        self.fp=open('mafengwo.json','w')

    def process_item(self, item, spider):
        text=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.fp.write(text.encode('utf-8','ignore'))
        return item

    def close_spider(self,spider):
        self.fp.close()
