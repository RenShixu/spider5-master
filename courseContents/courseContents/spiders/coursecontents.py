# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from courseContents.items import CoursecontentsItem


class CoursecontentsSpider(CrawlSpider):
    name = 'coursecontents'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/courses/k/p5']

    # Rule是在定义抽取链接的规则
    rules = (
        Rule(LinkExtractor(allow=('https://edu.csdn.net/course/detail/[0-9]+',)), callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        item = CoursecontentsItem()
        item['url'] = response.url
        print(item)
        return item
