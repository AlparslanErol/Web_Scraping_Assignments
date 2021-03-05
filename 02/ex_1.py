from urllib import request as re
from bs4 import BeautifulSoup as BS

url = 'http://www.pythonscraping.com/pages/page3.html'
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

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
