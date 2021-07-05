def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def print_lyrics():
    print('Hello Kabira!!')
repeat_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)
print_twice('Spam')
print_twice(12)

import math
print_twice(math.pi)

print_twice('Spam '*4)

print_twice(math.cos(math.pi))

michael = 'Eric, half a bee.'

print_twice(michael)

#fruitful function -- it return a value

x= math.sqrt(16)
print(x)

# void function - don't have a return valu. if you try to assign the result to a variable , you get a special value called 'None'

result = print_twice('Bing')

print(result)

print(type(None))

def addtwo(a,b):
    added = a + b
    return added

x = addtwo(14,12)
print(x)
