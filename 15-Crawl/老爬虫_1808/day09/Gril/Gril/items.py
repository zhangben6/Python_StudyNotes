# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GrilItem(scrapy.Item):
    # define the fields for your item here like:
    # 图片链接
    imgUrl = scrapy.Field()

