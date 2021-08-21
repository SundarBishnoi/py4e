##### Dictionary ######
#list has indexes and dictionary has keys.
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


#The get method for dictionary
#get method will give current value of key in dictionary and gives default value if key is not present in dictionary
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

#Counting pattern, it builds up 
counts = dict()
print('Enter the line of text to be counted on: ')
line = input(' ')
words =  line.split()
print('Words:', words)
print('Counting...')
for word in words :
    counts[word] = counts.get(word,0) + 1
print(counts)

#Definite loops and Dictionaries
for key in counts:
    print(key, counts[key])

#Retrieving lists of Keys and Values
print(counts)
print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())

#BONUS: Two Iteration Variables!
jjj = {'chuck':1, 'fred':42, 'jan':100}
for aaa, bbb in jjj.items() :
    print(aaa,bbb)

#Goal is to get the word that is used for max times in file.
name = input('Enter File Name: ')
name = "D:\python\py4e\ex_02_07_01\\" + name
counts = dict()
fhandle = open(name)
for line in fhandle:
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1

bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word

print(bigWord,bigCount)
