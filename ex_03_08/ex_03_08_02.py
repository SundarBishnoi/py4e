x = list()
type(x)
dir(x)

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

some =[1,12,34,21,5,9]
print(9 in some)
print(15 in some)
print(22 not in some)

friends = ['serum','reddy','albert']
friends.sort()
print(friends)

total = 0
count = 0
while True :
    inp = input('Enter number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average =0
try :
    average = total/count
except:
    print('please enter number')
print('Average: ', average)
numlist = list()
while True :
    inp = input('Enter number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average: ', average)
