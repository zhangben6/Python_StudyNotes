# -*- coding: utf-8 -*-
import scrapy
# 导入提取页面链接的类
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Tengxun.items import TengxunItem

class TengxunSpider(CrawlSpider):
    name = 'tengxun'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'),
             callback='parseTencent',
             follow=True),
        # Rule(LinkExtractor(allow=r'adkfd'),
        #      callback='parse2',
        #      follow=True)
    )

    def parseTencent(self, response):
        # 创建item对象
        item = TengxunItem()
        # 每个职位节点对象列表
        baseList = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for base in baseList:
            item['zhName'] = base.xpath('./td[1]/a/text()').extract()[0]
            item['zhType'] = base.xpath('./td[2]/text()').extract()
            # 部分页面职位类型为 空,在此做判断
            if item['zhType']:
                item['zhType'] = item['zhType'][0]
            else:
                item['zhType'] = "无"
            item['zhNum'] = base.xpath('./td[3]/text()').extract()[0]
            item['zhAddress'] = base.xpath('./td[4]/text()').extract()[0]
            item['zhTime'] = base.xpath('./td[5]/text()').extract()[0]
            item['zhLink'] = base.xpath('./td[1]/a/@href').extract()[0]

            yield  item
