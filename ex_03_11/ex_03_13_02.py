#JSON
import json
#JSON represnts data as nested "lists" and "dictionaries"
data = '''{
    "name" : "Chuck", 
    "phone" : {"type" : "intl", "number" : "+1 715 846 2143"},
    "email" : {"hide" : "yes"}
}'''

#by passing data object to loads method, we will get a dictionary.. so now we can access items as normal dictionary item

info = json.loads(data)
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])


input = '''[
    {"id" : "001","x" : "2","name" : "Chuck"}, 
    {"id" : "009","x" : "7","name" : "Chuck"}
    ]'''

#by passing input object to loads method, we will get a list.. so now we can access items as normal list item
info = json.loads(input)
print('USer Count: ', len(info))
for item in info:
    print('Name: ', item["name"])
    print('Id: ', item["id"])
    print('Attribute:', item['x'])
