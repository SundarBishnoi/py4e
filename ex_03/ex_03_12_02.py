import urllib.request, urllib.parse, urllib.error
fhand =  urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())

#Counting frequency of each words
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

#Parsing HTML using regualr expression
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

##just for reference to make regex pattern -- href="http://www.py4e.com/code3/urlregex.py"
#Search for link values within URL input
#above code snippet and this one, are similar
import re
import ssl
#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter --')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall('href="(http[s]?://.+?)"', html.decode())

for link in links:
    print(link)

#Reading binary files using urllib
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img) #this program reads all of the data in at once across the network and store in the variable img in the main memory of your computer, then opens the file cover.jpg and writes the data out to your disk. It will only work if the size of file is less than size of memory of your computer.
fhand.close()

#to avoid the running out of memory, we can retrieve the data in blocks(or buffers) and then write each block before retrieving next block
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand1 = open('newCover.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1 : break
    size = size + len(info)
    fhand1.write(info)

print('characters copied: ', size)
fhand.close()