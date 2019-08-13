    # -*- coding: utf-8 -*-
import scrapy
import json
from caipiao.items import CaipiaoCateItem

class AihuishouSpider(scrapy.Spider):
    name = 'caipiao'
    #allowed_domains = ['/kaijiang.zhcw.com']
    start_urls = ['http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html']
    def parse(self, response):
        pageCount = response.xpath("//table[@class='wqhgt']//tr/td/p[@class='pg']/strong/text()").extract_first()
        if pageCount :
            pageCount_int = int(pageCount)
            i = 1;
            while i <= pageCount_int:
                i+=1

                referer_url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_'+ str(i) + ".html"
                form_req = scrapy.Request(url=referer_url, meta={'item':referer_url},callback=self.caipiaoparse)
                form_req.headers['referer'] = referer_url
                yield form_req

    def caipiaoparse(self, response):
        print('-------------------------------')
        print('1')
        print('-------------------------------')
        tr_list = response.xpath("//table[@class='wqhgt']//tr")
        for tr_content in tr_list:
            td_list = tr_content.xpath(".//td")
            if len(td_list) > 3:
                openward_time = td_list[0].xpath(".//text()").extract_first()
                issue_number = td_list[1].xpath(".//text()").extract_first()
                numbers = td_list[2].xpath(".//em/text()").extract()
                caipiaoCateItem = CaipiaoCateItem()
                caipiaoCateItem['openward_time'] = openward_time
                caipiaoCateItem['issue_number'] = issue_number
                caipiaoCateItem['numbers'] = json.dumps(numbers)
                caipiaoCateItem['number1'] = numbers[0]
                caipiaoCateItem['number2'] = numbers[1]
                caipiaoCateItem['number3'] = numbers[2]
                caipiaoCateItem['number4'] = numbers[3]
                caipiaoCateItem['number5'] = numbers[4]
                caipiaoCateItem['number6'] = numbers[5]
                caipiaoCateItem['number7'] = numbers[6]
                yield caipiaoCateItem
