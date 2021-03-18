#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 18.03.2021 - 21:14

@author: ALPARSLAN
"""
from urllib import request
from bs4 import BeautifulSoup as BS
import pandas as pd
from dask.bytes.tests.test_http import requests
import re


def print_Exception(e):
    print(type(e))
    print(e.args)
    print(e)


url = 'https://en.wikipedia.org/wiki/Queen_(band)'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

df = pd.DataFrame({'Name': [], 'Genres': [], 'Years Active': []})

try:
    page_response = requests.get(url, timeout=5)
    if page_response.status_code == 200:
        try:
            name = bs.find('h1').text
            name = re.findall('(.*)\s\(band\)', name)[0]
        except Exception as e:
            print_Exception(e)
            name = ''

        try:
            genres = bs.find('th', string='Genres').next_sibling.text
        except Exception as e:
            print_Exception(e)
            genres = ''

        try:
            active_years = bs.find('th', string='Years active').next_sibling.text
        except Exception as e:
            print_Exception(e)
            active_years = ''

        queen = {'Name': name, 'Genres': genres, 'Years Active': active_years}
        df = df.append(queen, ignore_index=True)
        print(df)
    else:
        print(page_response.status_code)

except requests.Timeout as e:
    print("It is time to timeout")
    print(str(e))
