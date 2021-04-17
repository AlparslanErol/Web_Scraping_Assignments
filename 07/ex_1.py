#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 17.04.2021 - 17:45

@author: ALPARSLAN
"""
from selenium import webdriver
import time
import getpass
import datetime


gecko_path = 'C:\\Program Files\\Mozilla Firefox\\geckodriver.exe'
url = 'http://campuswire.com/signin'

options = webdriver.firefox.options.Options()
options.headless = False

driver = webdriver.Firefox(options=options, executable_path=gecko_path)

driver.get(url)
print(driver.page_source)

time.sleep(1)

username = driver.find_element_by_xpath('//input[@placeholder="Email"]')
my_email = input('Please provide your email:')
username.send_keys(my_email)

time.sleep(1)

password = driver.find_element_by_xpath('//input[@placeholder="password"]')
my_pass = getpass.getpass('Please provide your password:')
password.send_keys(my_pass)

time.sleep(1)

button = driver.find_element_by_xpath('//button[@type="submit"]')
button.click()

time.sleep(5)
print(driver.page_source)

search = driver.find_element_by_xpath('/html/body/div[1]/div/aside[1]/div/div[1]/ul/li[3]/button/span')
search.click()

time.sleep(1)
print(driver.page_source)

search_area = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[2]/input')
search_person = input('Please provide who you want to search:')
search_area.send_keys(search_person)

time.sleep(2)

people = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/ul/li[3]')
people.click()

time.sleep(1)

profile = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[4]/div[2]/div')
profile.click()

time.sleep(2)
print(driver.page_source)

timestamp = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")

driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea')\
    .send_keys(f"Hello Mrs. {search_person}, I am a little bot who is under duty of submitting"
               f" Alparslan's homework (basically myself :)!\n")
time.sleep(0.3)
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea')\
    .send_keys('I messaged at: ' + timestamp + '\n')
time.sleep(0.3)
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea')\
    .send_keys('I was run by: ' + my_email + '\n')
time.sleep(0.3)
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea')\
    .send_keys('You can find the .py file below...' + '\n')

time.sleep(2)

file = driver.find_element_by_xpath('//input[@type="file"]')
file_path = 'C:\\Users\\ALPARSLAN\\Desktop\\UW\\SEMESTER_2\\Webscraping and Social Media Scraping' \
            '\\Assignment\\assignment_submissions-AlparslanErol\\07\\ex_1.py'
file.send_keys(file_path)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea')\
    .send_keys('See you, wish you a good day :)' + '\n')

time.sleep(10)
print(driver.page_source)

driver.quit()
