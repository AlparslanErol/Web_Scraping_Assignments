#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 11.03.2021 - 23:15

@author: ALPARSLAN
"""
################################################################################
# Homework - 2
# Exercise - 2 Flags (Medium)
################################################################################

from urllib import request
from bs4 import BeautifulSoup as BS
from dask.bytes.tests.test_http import requests
import re

# Lets download and import to Beautiful Soup already known page:
url = 'https://en.wikipedia.org/wiki/United_Nations_Development_Programme'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

try:
    page_response = requests.get(url, timeout=5)
    if page_response.status_code == 200:
        # Now we search for images by regex:
        flags = bs.find_all('span', {'class': 'flagicon'})

        for flag in flags:
            f = flag.find('img', {'src': re.compile('.*')})
            country = re.compile('_of_(.*).svg/').findall(f['src'])[0]
            print(f'Path of {country} flag is..:\n{f["src"]}\n')
    else:
        print(page_response.status_code)

except requests.Timeout as e:
    print("It is time to timeout")
    print(str(e))
