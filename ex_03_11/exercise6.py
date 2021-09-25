import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


api_key = 42
service_url = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location -- ')
param = {'address': address, 'key':api_key}
#param variable is dict which is passed to urlencoded function.
#to convert into encoded url 
url = service_url + urllib.parse.urlencode(param)
print(url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved ', len(data), 'characters')

js = json.loads(str(data))


print(js['results'][0]['place_id'])