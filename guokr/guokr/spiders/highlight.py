# -*- coding: utf-8 -*-
import scrapy


class HighlightSpider(scrapy.Spider):
    name = 'highlight'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/']

    def parse(self, response):

    	def extract_by_css(query,extraction): 
    		result=extraction.css(query).extract_first()
    		if not result:
    			return None
    		return result.strip()

    	ask_lists=response.css('.ask-list-cp li')

    	# print u'*******'*10,len(ask_lists)
    
        for ask_list in ask_lists:

        	yield dict(
        	ask_focus_nums=extract_by_css('.ask-focus-nums  span::text',ask_list),
        	ask_answer_nums=extract_by_css('.ask-answer-nums  span::text',ask_list),
        	ask_list_question=extract_by_css('h2 a::text',ask_list),## text 得到的是最末节点的内容
        	ask_list_href=ask_list.css('h2 a::attr(href)').extract_first(),
        	ask_list_summary=extract_by_css('.ask-list-summary ::text',ask_list),
        	ask_list_tags=','.join(ask_list.css('.tags a::text').extract()), ##全部转化成字符串
        	)
        next_page=response.css('.gpages li a::attr(href)')[-2]
        print u'&&&&&&&'*10,next_page
        yield response.follow(url=next_page,callback=self.parse)