# To run this, you can install BeautifulSoup
# htpps//pypi.python.org/pypi/beautifulsoup4

# or download the file
# htpps/www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
form bs4 improt BeautifulSoup
improt ssl

# Ignore SSL ertificate errors
ctx = ssl.creat_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.requese.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

