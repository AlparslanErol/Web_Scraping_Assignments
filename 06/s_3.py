#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 10.04.2021 - 00:04

@author: ALPARSLAN
"""
import scrapy


class Musician(scrapy.Item):
    name = scrapy.Field()
    years_active = scrapy.Field()


class LinksSpider(scrapy.Spider):
    name = 'musicians'
    allowed_domains = ['https://en.wikipedia.org/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        m = Musician()
        name_xpath = '//h1/text()'
        m['name'] = response.xpath(name_xpath).getall()

        years_active_xpath = "//th/span[contains(text(), 'Years active')]/../following-sibling::*/text()"
        m['years_active'] = response.xpath(years_active_xpath).getall()
        if not m['years_active']:
            years_active_xpath = '//th/span[contains(text(),"Years active")]/following::td[1]/div/ul/li/text()[1]'
            m['years_active'] = response.xpath(years_active_xpath).getall()

            if not m['years_active']:
                years_active_xpath = '//th[contains(text(),"Years")]/following::td[1]/text()'
                m['years_active'] = response.xpath(years_active_xpath).getall()

        if '\n' in m['years_active']:
            years_active_xpath = '//th/span[contains(text(),"Years active")]/following::td[@class = "infobox-data"][1]/ul/li/text()'
            m['years_active'] = response.xpath(years_active_xpath).getall()

        yield m
