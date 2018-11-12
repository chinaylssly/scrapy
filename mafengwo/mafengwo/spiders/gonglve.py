# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings
from mafengwo.items import MafengwoItem


class GonglveSpider(scrapy.Spider):
    name = 'gonglve'
    allowed_domains = ['mafengwo.cn']
    # custom_settings={'user-agent':'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0'}#优先于settings.py，调用custom_setttings将不会调用settings.py
    start_page=1

    def post_request(self):
    	url='http://www.mafengwo.cn/gonglve/' 
    	print u'current page is:',self.start_page	
    	data={'page':str(self.start_page)}
    	return scrapy.FormRequest(url=url,formdata=data,callback=self.parse)

    def start_requests(self):
    	while self.start_page<30:
    		yield self.post_request()
    		self.start_page+=1
    	

    def parse(self, response):
    	# print '#########3',response.body
    	def clear_text(bs_obj):
    		try:
    			return bs_obj.get_text().strip()
    		except Exception,e:
    			print u'error info:',e
    			return None

        soup=BeautifulSoup(response.body,'lxml')
        # print soup
        items=soup.find_all('div',attrs={'class':'feed-item _j_feed_item'})
        
        item=MafengwoItem()

        for i in items:

            # print str(i).decode('utf-8','ignore').encode('gb2312','ignore')

            num=i.find('span',attrs={'class':'num'})
            refer=i.find('span',attrs={'class':'type'})
            info=i.find('div',attrs={'class':'info'})
            title=i.find('div',attrs={'class':'title'})
            href=i.find('a')['href']
            author=i.find('span',attrs={'class':'author'})
            nums=i.find('span',attrs={'class':'nums'})

          

            item['num']=clear_text(num)
            item['refer']=clear_text(refer)
            item['info']=clear_text(info)
            item['title']=clear_text(title)
            item['href']=href
            item['author']=clear_text(author)
            item['nums']=clear_text(nums)

            yield item


if __name__ == '__main__':

    process=CrawlProcess(get_project_settings())
    process.crawl('gonglve')
    process.start()
			
    			
   