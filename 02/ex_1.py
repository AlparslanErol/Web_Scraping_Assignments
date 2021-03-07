from urllib import request as re
from bs4 import BeautifulSoup as BS
from dask.bytes.tests.test_http import requests

url = 'http://www.pythonscraping.com/pages/page3.html'
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

try:
    page_response = requests.get(url, timeout=5)
    if page_response.status_code == 200:
        # POINT 1
        print("Results for point 1...")
        for index in bs.find_all('span', {'class': "excitingNote"}):
            print(index.text)

        # POINT 2
        print("\nResults for point 2...")
        last_item_title = bs.find('tr', {'id': 'gift5'}).td.text
        print(last_item_title)

        # POINT 3
        print("\nResults for point 3...")
        footer = bs.find('div', {'id': 'footer'}).text
        print(footer)

    else:
        print(page_response.status_code)
except requests.Timeout as e:
    print("It is time to timeout")
    print(str(e))
