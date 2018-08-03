# -*- coding: utf-8 -*-
import json

import scrapy
from Pinduoduo.items import PinduoduoItem


class PinduoduoSpider(scrapy.Spider):
    name = 'pinduoduo'
    allowed_domains = ['yangkeduo.com']
    page = 1
    start_urls = [
        'http://apiv3.yangkeduo.com/v5/goods?page=' + str(
            page) + '&size=400&column=1&platform=1&assist_allowed=1&list_id=single_jXnr6K&pdduid=0']

    def parse(self, response):
        goods_list_json = json.loads(response.body)
        goods_list = goods_list_json['goods_list']
        # 判断是否是最后一页
        if not goods_list:
            return
        for each in goods_list:
            item = PinduoduoItem()
            item['goods_name'] = each['goods_name']
            item['price'] = float(each['group']['price']) / 100  # 拼多多的价格默认多乘了100
            item['sales'] = each['cnt']
            item['normal_price'] = float(each['normal_price']) / 100
            item['goods_id'] = each['goods_id']
            yield scrapy.Request(url="http://apiv3.yangkeduo.com/reviews/" + str(item['goods_id']) + "/list?&size=20",
                                 callback=self.get_comments, meta={"item": item})
        self.page += 1
        yield scrapy.Request(url='http://apiv3.yangkeduo.com/v5/goods?page=' + str(
            self.page) + '&size=400&column=1&platform=1&assist_allowed=1&list_id=single_jXnr6K&pdduid=0',
                             callback=self.parse)

    def get_comments(self, response):
        """默认每个商品只爬取20条商品评论"""
        item = response.meta["item"]
        comment_list_json = json.loads(response.body)
        comment_list = comment_list_json['data']
        comments = []
        for comment in comment_list:
            if comment["comment"] == "":
                continue
            comments.append(comment["comment"])
        item["comments"] = comments
        yield item
