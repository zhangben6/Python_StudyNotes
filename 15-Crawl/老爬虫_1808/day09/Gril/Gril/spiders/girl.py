# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import json
from Gril.items import GrilItem

class GirlSpider(scrapy.Spider):
    name = 'girl'
    allowed_domains = ['image.so.com']
    # 把start_urls去掉,重写start_requests()方法
    # 重写也就是自己指定要爬取的起始的URL地址
    def start_requests(self):
        baseurl = 'http://image.so.com/zj?'
        for pg in range(0,91,30):
            params = {
                'ch':'beauty',
                'sn': str(pg),
                'listtype':'new',
                'temp':'1',
            }
            # 给params进行编码
            params = urlencode(params)
            # params : 'ch=beauty&sn=0&list....'
            fullUrl = baseurl + params
            yield scrapy.Request(fullUrl,
                                callback=self.parse)


    def parse(self, response):
        item = GrilItem()
        # response.text是json格式的字符串,-> 字典
        imgList = json.loads(response.text)['list']
        # imgList : [{美女1},{美女2},{美女3}]
        for img in imgList:
            item['imgUrl'] = img['qhimg_url']
            yield item






