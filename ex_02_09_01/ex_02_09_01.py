##### Dictionary ######
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
#dictionaries are mutable
purse['candy'] =  purse['candy'] + 2
print(purse['candy'])

#Dictionary Literals(Constants)
jjj = {'chuck':1, 'fred': 14, 'jan': 16}
print(jjj)

ooo = {  }
print(ooo)


#Many Counters with a dictionary.
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

ppp = dict()
print('value' in ppp)

#When we see a new name, we need to add a new name entry in the dictionary and if this the second or the later time we have seen the name,
#we simply add one to the count in the dictionary under that name
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# The get method for dictionary
#get method will give current count
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
