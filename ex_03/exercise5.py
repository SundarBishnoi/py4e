import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sys

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location --- ')
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved ', len(data), 'characters.')

try:
    js = json.loads(data)
except:
    js = None

if not js:
    print('=====Failure to retrieve ========')
    print(data)
    sys.exit()

sum = 0

for item in js['comments']:
    sum += item['count']

print(sum)