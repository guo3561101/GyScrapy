# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'     #名字
    allowed_domains = ['itcast.cn']     #运训爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ac']  #最开始请求的url

    def parse(self, response):
        # for i in range(1,11):
        #     a = response.xpath('/html/body/div[1]/div[5]/div/div[2]/div[1]/ul/li[{}]/div[2]/h3/text()'.format(i)).extract()
        #     print(a)
        li_list = response.xpath('//div[@class="tea_con"]//li')
        for li in li_list:
            item={}
            item['name']= li.xpath('.//h3/text()').extract_first()
            item['title'] = li.xpath('.//h4/text()').extract_first()
            # print(item)
            yield item