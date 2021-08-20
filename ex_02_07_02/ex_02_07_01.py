
#----- Topics covered -----
#Secondary storage
#Searching for lines
#Opening a file - file handle
#Reading file names
#File structure  - new line character
#Dealing with bad files
#Reading a file line by line with a for loop


#files are stored in secondary storage(permanent)
#Reading a file
fhand = open('D:\python\py4e\ex_02_07_02\mbox.txt')
for line in fhand:
    line = line.rstrip()
    print(line)


#Reading  the *Whole* files  //we can read the whole file into a single string
#Reading the *Whole* File
#we can read the whole file(newlines and all) into a single string
fhand = open('D:\python\py4e\ex_02_07_02\mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:300])


#Counting Lines in a File
fhand = open('D:\python\py4e\ex_02_07_02\mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)

#Searching through a file
fhand = open('D:\python\py4e\ex_02_07_02\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

#Skipping with continue
fhand = open('D:\python\py4e\ex_02_07_02\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)

#Using in to select lines
fhand = open("D:\python\py4e\ex_02_07_02\mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if '@uct.ac.za' in line:
        print(line)

#Prompt for file name
fname = input("Enter the file name: ")
fname = 'D:\python\py4e\ex_02_07_02\\' + fname
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count+1
print('There were', count, 'subject lines in',fname)

#Dealing with Bad file names
fname = input('Enter the file name: ')
fname = 'D:\python\py4e\ex_02_07_02\\' + fname
try:
    fhand = open(fname)
except:
    print('file cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in',fname)