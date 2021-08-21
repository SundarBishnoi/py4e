#tuples has parenthesis ()

l = list()
d = dict()
t = tuple()

x = ('Glenn', 'Ramesh','Shyam')
print(x)
print(x[2])
y = (1,9,12)
print(y)

print(max(y))

for iter in y:
    print(iter)


#Tuples are immutable
x = [9,8,7]
x[2] = 15 #in list assignment works fine but not in strings and tuples
print(x)

#y = 'ABC'
#y[2] = 'D'
#print(y)

#z = (5,4,16)
#z[2] = 0
#print(z)


#Things not to do with Tuples
x = (3,12,4)
#x.sort()

#x.append(5)
#x.reverse()

# Tuples and Assignment 
(x,y) = (4,'fred')
print(y)

(a,b) = (99,88)
print(a)

#Tuples and Dictionaries
d = dict()
d['dict'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

print((0,1,2)< (5,1,2))

l = list()
t = tuple()
#print(dir(l))
#print(dir(t))

#sorting lists of tuples

d = {'a':11 ,'c':22, 'b':1} 
print(d.items())
print(sorted(d.items()))

#Using sorted()

for (k,v) in sorted(d.items()):
    print(k,v)

#Sort by values Instead of Keys
c = {'a':10, 'b':1,'c':22}
tmp = list()
for k, v in (c.items()) :
    tmp.append((v,k))
print(tmp)

for k,v in sorted(tmp,reverse=True):
    print(k,v)

###The top 10 most common words in romeo.txt
path = 'D:\python\py4e\ex_02_08_01\\romeo.txt'
fhandle = open(path)
bag = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        bag[word] = bag.get(word,0) + 1

temp = list()   

for k,v in bag.items():
    temp.append((v,k))

temp = sorted(temp, reverse=True)

for val, key in temp[:10]:
    print(key, val)

# -- shorter version of above code 
#List Comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.

c = {'a':10, 'b':1,'c':22}
print(sorted([(v, k) for (k, v) in c.items()]))