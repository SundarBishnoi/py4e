#Lists
# List constants are surrounded by square brackets
from typing import TYPE_CHECKING


print([9,21,13])
print(['red','yellow','white'])
print(['red',21,'white',98.6])
print(['yellow',[24,12],15]) 
print([])

for i in [5,3,15,12,6]:
    print(i)
print('blast off!')

#List and definite loops
friends = ['Joseph','Glenn','Sally']
for friend in friends:
    print('Happy new year:', friend)
print('Done!')

z = ['Joseph','Glenn','Sally']
for x in z:
    print('Happy new year:',x)
print('Done!')

#Looking inside Lists
friends = ['Joseph','Glenn','Sally']
print(friends[1])

#Lists are mutable i.e. it can be changed but strings are immutable (we cann't change the content of a string.)

fruit = 'Banana'
#fruit[0] = 'b'
x = fruit.lower()
print(x)

lotto = [24,15,16,18]
print(lotto)
lotto[2]=28
print(lotto)

#Lists have length, just like strings.
friend = 'Rohan Boy'
print(len(friend))
x = [1,2 ,'boy',15]
print(len(x))

#Using the Range function -- range funtion returns a list of numbers from zero to one less than parameter
print(range(4))

friends = ['Joseph','Glenn','Sally']
print(len(friends))
print(range(len(friends)))

for x in friends:
    print('Happy new year:', x)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year:', friend)

#Concatenating Lists using +
a = [1,2,3]
b= [4,5,6]
c = a+b
print(c)
print(a)

#Lists can be Sliced Using :
t = [9,12,41,54,18]
#just like in strings , the second number is 'up to but not including'
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])


#Building a List from Scratch
#append will add the item in the end of list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

#is something 'in' a list or 'not in'??
some = [1,15,18,21,30]
print(15 in some)
print(12 in some)
print(20 not in some)

friends = ['Joseph','Glenn','Sally']
friends.sort()
print(friends)
print(friends[1])

#Built-in Functions and Lists

nums = [3,14,26,9,74,56,18]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

######Strings and Lists######

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)

#
line = 'A lot         of spaces'
etc = line.split()
print(etc)
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';')
print(thing)
print(len(thing))

#parsing mail data
#Goal is to find the days of week when we received mail 
#From wagnermr@iupui.edu Fri Jan  4 10:38:42 2008
fhand = open('D:\python\py4e\ex_02_07_02\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
 #   print(words)

#The Double Split Pattern

line = 'From wagnermr@iupui.edu Fri Jan  4 10:38:42 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])