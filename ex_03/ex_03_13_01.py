import xml.etree.ElementTree as ET

data = '''
    <person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes"/>
    </person>
'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print(tree.find('email').get('hide'))
print(tree.find('phone').text.strip())


#------------------

#Looping through Nodes 
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
#findall method will store as list of tree/nodes.
lst = stuff.findall('users/user')
print('User Count: ', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
