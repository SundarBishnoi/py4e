#String Concatenation
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)

#Using in as a logical operator
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print('Found it..')

#############         String Library          #############
#variable greet is string object, we invoke its method by appending to string object with . 
greet = 'Hello Bob'
print(type(greet))
zap = greet.lower()
print(zap)
print(greet)
print('Hi there'.lower())

stuff = 'Hello world'
type(stuff)
#Methods in Class str can be displayed using dir
dir(stuff)
#capitalize the string 
stuff.capitalize()
#searching a string using find function
fruit  = 'banana'
pos =  fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

#Making everything upper case
greet = 'Hello Bob'
nnn =  greet.upper()
print(nnn)
#Making everything lower case
www = greet.lower()
print(www)

#Search and Replace
greet = 'Hello Bob'
nstr =  greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o','X')
print(nstr)

#Stripping whitespaces
greet = '   Hello Bob   '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

#Prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

#Parsing and Extracting
data =  'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
sppos = data.find(' ', atpos)
host = data[atpos+1:sppos]
print(host)

#--Topics covered--
#String types
#Read/Convert
#Indexing strings
#Slicing strings [2:4]
#Looping through strings with for and while
#Concatenating strings with +
#String operations
#String Library
#String comparisions
#Searching in strings
#Replacing text
#Stripping whitespaces