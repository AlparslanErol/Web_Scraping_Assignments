################################################################################
# Regex + Beautiful Soup.
################################################################################
# This script shows how to use powerful regex as another tool to navigate tags

from urllib import request
from bs4 import BeautifulSoup as BS
import re

# Lets download and import to Beautiful Soup already known page:
url = 'https://en.wikipedia.org/wiki/United_Nations_Development_Programme'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

# Now we search for images by regex:
flags = bs.find_all('span', {'class': 'flagicon'})

for flag in flags:
    f = flag.find('img', {'src': re.compile('.*')})
    country = re.compile('_of_(.*).svg/').findall(f['src'])[0]
    print(f'Path of {country} flag is..:\n{f["src"]}\n')

################################################################################
# Experiment with code on your own.
# Can you extract all prices using regex? Directly? Indirectly?
