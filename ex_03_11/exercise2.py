import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

numbers = []

url = input('Enter ---')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
count = 0
sum = 0
for tag in tags:
    sum=sum+int(tag.contents[0])
    #print(tag.contents[0])
    count +=1
print(count)
print(sum)