#looping through strings using indefinite loop
fruit = 'banana'
index =0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index+1
#--------------------
#looping through strings using definite loop
fruit =  'banana'
for letter in fruit:
    print(letter)

#looping and counting the occurance of a particular character in string
fruit = 'banana'
count = 0
for letter in fruit:
    if letter is 'a':
        count = count + 1
print(count)

#Slicing strings -- we can also look at the continuous section of a string using a colon operator
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])