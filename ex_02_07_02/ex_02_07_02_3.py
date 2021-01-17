#searching through a file (fixed)
fhand = open('mob.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('Orange'):
        print(line)
