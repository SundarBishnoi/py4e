#skipping with continue
fhand = open('mob.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('Orange'):
        continue
    print(line)
