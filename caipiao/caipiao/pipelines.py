# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymysql.cursors
from caipiao.items import CaipiaoCateItem
class CaipiaoPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='spider',  # 数据库名
            user='root',  # 数据库用户名
            passwd='root',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

        self.questionitem = [];
        self.optionitem  = [];
        self.list_limit = 1000;

    def process_item(self, item, spider):
        if isinstance(item,CaipiaoCateItem) :
            self.caipiaoPipelineCate( item, spider)
        else:
            return item

    def caipiaoPipelineCate(self, item, spider) :
        info = self.cursor.execute("select id from caipiao where issue_number = (%s)", item['issue_number'])
        if info == 0:
            self.cursor.execute("insert into caipiao(openward_time,issue_number,number1,number2,number3,number4,number5,number6,number7,numbers) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                             (item['openward_time'],item['issue_number'],item['number1'],item['number2'],item['number3'],item['number4'],item['number5'],item['number6'],item['number7'],item['numbers']))
