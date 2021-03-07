from urllib import request as re
from bs4 import BeautifulSoup as BS
from datetime import datetime
from dask.bytes.tests.test_http import requests

url = 'https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a'
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

try:
    page_response = requests.get(url, timeout=5)
    if page_response.status_code == 200:
        # POINT 1
        print("Results for point 1...")
        birthdate = bs.find('span', {'class': 'noprint ForceAgeToShow'}).parent.span.text[2:-2]

        # Scrapped string from website directly.
        print("Scrapped string from website is {}".format(birthdate))

        # Scrapped string converted datetime format.
        date = datetime.strptime(birthdate, '%Y-%m-%d')
        print("Scrapped string converted datetime format as {}".format(date))

        # Converted datetime format printed like... Month day, Year format
        date1 = date.strftime("%d %B %Y")
        print("Converted datetime format printed like in website is...\n{}".format(date1))

        # POINT 2
        print("\nResults for point 2...")
        for index, occupation in enumerate(bs.find('div', {'class': 'hlist hlist-separated'}).ul.find_all('li')):
            print("Occupation number {} is {}".format(index + 1, occupation.text))

        # POINT 3
        print("\nResults for point 3...")
        for index, reference in enumerate(bs.find_all('span', {'class': 'reference-text'})):
            print("Reference {}..: {}\n".format(index + 1, reference.text))

    else:
        print(page_response.status_code)
except requests.Timeout as e:
    print("It is time to timeout")
    print(str(e))
