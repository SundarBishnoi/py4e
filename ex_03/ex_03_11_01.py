### Regular Expressions...
import re 
# Using re.search() Like find()
fhandle = open('D:\python\py4e\ex_02_07_02\mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if line.find('From: ') >= 0:
        print(line)

print('**********************************')

fhandle1 = open('D:\python\py4e\ex_02_07_02\mbox-short.txt')
for line in fhandle1:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)

#Using re.search() Like startswith()

fhandle2 = open('D:\python\py4e\ex_02_07_02\mbox-short.txt')
for line in fhandle2:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

fhandle3 = open('D:\python\py4e\ex_02_07_02\mbox-short.txt')
for line in fhandle3:
    line = line.rstrip()
    if re.search('^From: ', line):
        print(line)


#Matching and extracting data
x = 'From: My 2 favorite numbers are 19 and 12 sundar@gmail.com  '
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[AEIOU]+', x)
print(y)

# Greedy Matching
y = re.findall('^F.+:', x)
print(y)
# Non Greedy Matching
y = re.findall('^F.+?:', x)
print(y)

# Fetching non whitespace character
y = re.findall('\S+@\S+',x)
print(y)

y = re.findall('(\S+?@\S+)', x)
print(y)
y = re.findall('@([^ ]*)', x)
print(y)
y = re.findall('^From: .*@([^ ]*)', x)
print(y)

lin = 'Price for mango has increased to $10.85'
y = re.findall('\$[0-9.]+', lin)
print(y)