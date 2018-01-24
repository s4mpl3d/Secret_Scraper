# -*- coding: utf-8 -*-
import scrapy


class PastebinSpider(scrapy.Spider):
    name = 'pastebin'
    allowed_domains = ['pastebin.com']
    start_urls = ['http://pastebin.com/']

    def parse(self, response):
        pass
