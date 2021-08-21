#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


fhandle = open('D:\python\py4e\ex_02_07_02\\mbox-short.txt')

hours = list()
counts = dict()
for line in fhandle:
    if line.startswith('From '):
        hours = line.split()
        hour = hours[5]
        hour = hour[:2]
        counts[hour] = counts.get(hour,0) + 1


print(counts)

for (k,v) in sorted(counts.items()):
    print(k,v)