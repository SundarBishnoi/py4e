import urllib.request, urllib.parse, urllib.error
fhand =  urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())


counts = dict()
fhand =  urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().split()
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
print(counts)


#reading html files

fhand =  urllib.request.urlopen('http://www.dr-chuck.com/page1.html')

for line in fhand:
    print(line.decode().strip())


#using regular expression, find all the links referenced on html page and store them into a list
import re
fhand =  urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
hrefList = list()
for line in fhand:
    newList = re.findall('href="(\S+\S)">', line.decode().strip())
    if len(newList) > 0:
    #    hrefList.append(newList)
        hrefList += newList
        
print(hrefList)


