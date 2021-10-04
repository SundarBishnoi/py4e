import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter ----')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


#to pull out various parts of each tag
for tag in tags:
    print('TAG: ', tag)
    print('URL: ', tag.get('href', None))
    print('Contents: ', tag.contents[0])
    print('Attrs: ', tag.attrs)

## 'html.parser' is the HTML parser included in the standard python 3 library
