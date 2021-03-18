#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 18.03.2021 - 20:26

@author: ALPARSLAN
"""
from urllib import request
from bs4 import BeautifulSoup as BS
from dask.bytes.tests.test_http import requests
import re


def print_Exception(e):
    print(type(e))
    print(e.args)
    print(e)


# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/List_of_rock_music_performers'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

try:
    page_response = requests.get(url, timeout=5)
    if page_response.status_code == 200:
        regex = re.compile('[Q]')
        regex_1 = re.compile('href="(.*)"\s')
        try:
            tags = bs.find('span', {'id': regex}).parent.next_sibling.next_sibling
        except Exception as e:
            print_Exception(e)
            tags = ''
        try:
            links = re.findall(regex_1, str(tags))
        except Exception as e:
            print_Exception(e)
            links = ''

        for link in links:
            print('http://en.wikipedia.org' + link)
    else:
        print(page_response.status_code)

except requests.Timeout as e:
    print("It is time to timeout")
    print(str(e))
