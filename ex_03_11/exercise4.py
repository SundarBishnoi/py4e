import xml.etree.ElementTree as ET
import urllib.parse, urllib.request, urllib.error

url = input('Enter---- ')
line = urllib.request.urlopen(url).read()

#this will give us xml object from the string data
xmldata = ET.fromstring(line)
lst = xmldata.findall('comments/comment')

sum = 0

counts = xmldata.findall('.//count')
#for item in lst:
#    sum = sum + int(item.find('count').text)

for v in counts:
    sum += int(v.text)


print(sum)
