#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 25.03.2021 - 22:15

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


url = 'https://en.wikipedia.org/wiki/Lists_of_musicians'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

df = pd.DataFrame({'Name': [], 'Genres': [], 'Years Active': []})

try:
    page_response = requests.get(url, timeout=5)
    if page_response.status_code == 200:
        ################################################################################
        # This part prepares preliminary links - links for lists of links :)
        ################################################################################
        regex = re.compile('[A]')
        regex_1 = re.compile('href="(.*)"\s')

        try:
            tags = bs.find('span', {'id': regex}).parent.next_sibling.next_sibling.next_sibling.ul
        except Exception as e:
            pass
            #print_Exception(e)
            tags = ''

        try:
            links = re.findall(regex_1, str(tags))
        except Exception as e:
            pass
            #print_Exception(e)
            links = ''

        final = ['http://en.wikipedia.org' + link for link in links]

        ################################################################################
        # This part prepares real painter links
        ################################################################################
        musician_links = []

        for link in final:
            print(link)
            html = request.urlopen(link)
            bs = BS(html.read(), 'html.parser')

            link_temp_list = []
            try:
                uls = bs.find_all('ul')
            except:
                continue

            # If you want to extract data from all links inside the musicians page, uncomment following code and
            # comment the code [79 - 87]. Current version scrap first's musician's data links in all genre.
            # for ul in uls:
            #     for li in ul.find_all('li'):
            #         try:
            #             #print('http://en.wikipedia.org' + li.a['href'])
            #             link_temp_list.append('http://en.wikipedia.org' + li.a['href'])
            #         except Exception as e:
            #             continue
            #             #print_Exception(e)
            #             link_temp_list.append('')

            for li in uls[1].find_all('li'):
                try:
                    #print('http://en.wikipedia.org' + li.a['href'])
                    link_temp_list.append('http://en.wikipedia.org' + li.a['href'])
                except Exception as e:
                    continue
                    #print_Exception(e)
                    link_temp_list.append('')

            musician_links.extend(link_temp_list)

            print(len(musician_links))

            for musician_link in musician_links:
                try:
                    html = request.urlopen(musician_link)
                    bs = BS(html.read(), 'html.parser')
                except:
                    continue
                try:
                    name = bs.find('h1').text
                except Exception as e:
                    #print_Exception(e)
                    name = ''

                try:
                    genres = bs.find('th', string='Genres').next_sibling.text
                except Exception as e:
                    #print_Exception(e)
                    genres = ''

                try:
                    active_years = bs.find('th', string='Years active').next_sibling.text
                except Exception as e:
                    #print_Exception(e)
                    active_years = ''

                queen = {'Name': name, 'Genres': genres, 'Years Active': active_years}
                df = df.append(queen, ignore_index=True)
            print(df)

        ################################################################################
        # This part saves data to csv.
        ################################################################################
        df.to_csv('musicians.csv')

    else:
        print(page_response.status_code)

except requests.Timeout as e:
    print("It is time to timeout")
    print(str(e))
