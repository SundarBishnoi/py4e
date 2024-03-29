#Google geocoding web service
#We are going to connect with Google MAP API to retrive the JSON Format Data back to us where we have to provide one parameter i.e. Address.
#https://maps.googleapis.com/maps/api/geocode/outputFormat?parameters

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = '42'
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location----')
    if len(address) < 1: break

    param = dict()
    param['address'] = address

    if api_key is not False: param['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(param)

    print('Retrieving ', url)
    
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    #print((js['results']))
    if not js or 'status' not in js or js['status'] != 'OK':
        print('=====Failure to retrieve ========')
        print(data)
        continue

    print(js['results'][0]['place_id'])
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

