#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 9.04.2021 - 03:57

@author: ALPARSLAN
"""
import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'link_lists'
    allowed_domains = ['https://en.wikipedia.org/']
    start_urls = ['https://en.wikipedia.org/wiki/Lists_of_musicians']

    def parse(self, response):
        xpath = '///html/body/div[3]/div[3]/div[5]/div[1]/div[4]/ul/li/a//@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://en.wikipedia.org' + s.get()
            yield l
