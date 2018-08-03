# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from Pinduoduo.items import PinduoduoItem

from pymongo import MongoClient


class PinduoduoGoodsPipeline(object):
    """将商品详情保存到MongoDB"""

    def open_spider(self, spider):
        self.db = MongoClient(host="127.0.0.1", port=27017)
        self.client = self.db.Pinduoduo.pinduoduo

    def process_item(self, item, spider):
        if isinstance(item, PinduoduoItem):
            self.client.insert(dict(item))
        return item
