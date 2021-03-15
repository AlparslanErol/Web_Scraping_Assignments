#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 15.03.2021 - 02:15

@author: ALPARSLAN
"""
################################################################################
# Homework - 2
# Exercise - 1 War and Peace (Easy)
################################################################################

from urllib import request
from bs4 import BeautifulSoup as BS

# Download and import to Beautiful Soup already known page:
url = 'http://www.pythonscraping.com/pages/warandpeace.html'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

# Point 1
selected_tags_1 = bs.find_all(lambda tag: ('Anna Pavlovna' in tag.get_text()))

# To print out tag content with include 'Anna Pavlovna', uncomment following lines.
# for tag in selected_tags_1:
#     print('*****************')
#     print(tag.get_text())

print(f"Point 1:\nAnna Pavlovna appears {len(selected_tags_1)} times in the text.")

# Point 2
selected_tags_2 = bs.find_all(lambda tag: (len(tag.attrs) == 1))

# To print out enlisted tags with exactly one attribute, uncomment following lines.
# for tag in selected_tags_2:
#     print('*****************')
#     print(tag.get_text())

print(f"Point 2:\nLength of tags with exactly one attribute is..: {len(selected_tags_2)}.")
