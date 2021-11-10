import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
key = 'AIzaSyCvK5om_l8BgHnUym5O9Ayxj0MqyWqiAMw'

while True:
    address = input('Enter location: ')

    if len(address) < 1: break
    url = serviceurl + urllib.parse.urlencode({'address': address})
    url = url + '&key=' + 'AIzaSyCvK5om_l8BgHnUym5O9Ayxj0MqyWqiAMw'

    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retreived ', len(data), 'characters')

    try :
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('-----Failure to retrieve-----')
        print(data)
        continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat ', lat, 'lng ', lng)
    location = js['results'][0]['formatted_address']
    print(location)
