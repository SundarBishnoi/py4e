#prompt for filename
fname = input('Enter file name: ')
fhand = open(fname)
count =0
for line in fhand:
    if line.startswith('text'):
        count = count+1
print('There were', count, 'line that starts with in',fname)
