#Searching through a file
fhand = open('mob.txt')
for line in fhand:
    if line.startswith('Orange'):
        print(line)
