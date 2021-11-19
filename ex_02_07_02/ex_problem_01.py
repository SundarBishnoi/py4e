#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.


fname = input("Enter file name: ")
fname = 'D:\python\py4e\ex_02_07_02\\' + fname
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    print(line.upper())
