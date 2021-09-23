import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def followedLink(url, position_wrt_first, no_of_repetition):
    nameList = list()
    links = []
    while True:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        url = soup.find_all('a')[position_wrt_first-1].get('href', None)
        no_of_repetition -= 1
        if no_of_repetition == 0: 
            name = soup.find_all('a')[position_wrt_first-1].contents[0]
            return name


url = input('Enter---')
position_wrt_first = int(input('Enter position wrt first ---'))
no_of_repetition = int(input('enter repition---'))

print(followedLink(url, position_wrt_first, no_of_repetition))