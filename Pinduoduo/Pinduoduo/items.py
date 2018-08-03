# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PinduoduoItem(scrapy.Item):
    # define the fields for your item here like:
    goods_id = scrapy.Field()
    goods_name = scrapy.Field()
    price = scrapy.Field()  # 拼团价格 返回的字段多乘了100
    sales = scrapy.Field()  # 已拼单数量
    normal_price = scrapy.Field()  # 单独购买价格
    comments = scrapy.Field()
