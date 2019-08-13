# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CaipiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CaipiaoCateItem(scrapy.Item):
    # define the fields for your item here like:
    openward_time = scrapy.Field()  #
    issue_number = scrapy.Field()  #
    number1 = scrapy.Field()  #
    number2 = scrapy.Field()  #
    number3 = scrapy.Field()  #
    number4 = scrapy.Field()  #
    number5 = scrapy.Field()  #
    number6 = scrapy.Field()  #
    number7 = scrapy.Field()  #
    numbers = scrapy.Field()  #
