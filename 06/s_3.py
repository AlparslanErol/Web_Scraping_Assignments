#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 10.04.2021 - 00:04

@author: ALPARSLAN
"""
import scrapy


class Musician(scrapy.Item):
    name = scrapy.Field()
    year_active = scrapy.Field()


class LinksSpider(scrapy.Spider):
    name = 'musicians'
    allowed_domains = ['https://en.wikipedia.org/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        p = Musician()
        name_xpath = '//h1/text()'
        year_active_xpath = '//span[text()="Years active"]/../following-sibling::*/text()'

        p['name'] = response.xpath(name_xpath).getall()
        p['year_active'] = response.xpath(year_active_xpath).getall()

        yield p
