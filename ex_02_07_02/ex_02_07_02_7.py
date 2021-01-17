#dealing with bad file names
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('file cannot be opened:',fname)
    quit()
count =0
for line in fhand:
    if line.startswith('text'):
        count = count+1
print('There were', count, 'line that starts with in',fname)
