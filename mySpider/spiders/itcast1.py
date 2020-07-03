# -*- coding: utf-8 -*-
import scrapy


class Itcast1Spider(scrapy.Spider):
    name = 'itcast1'
    allowed_domains = ['https://www.suning.com/']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        pass
