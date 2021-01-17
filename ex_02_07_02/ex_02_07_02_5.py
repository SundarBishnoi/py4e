#using in to select lines
fhand = open('mob.txt')
for line in fhand:
    line = line.rstrip()
    if not 'data' in line:
        continue
    print(line)
