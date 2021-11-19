#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values 
# and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter file name: ")
fname = 'D:\python\py4e\ex_02_07_02\\' + fname
total =0
count =0
fhand = open(fname)
for line in fhand:
    if 'X-DSPAM-Confidence' in line:
        fpos = line.find('0')
        value = float(line[fpos:])
        count = count +1
        total = total + value
 
print('Average spam confidence:', total/count)