#reading  the *whole * files  //iwe can read the whole file into a single string
fhand = open('mob.txt')
inp = fhand.read()
print(len(inp))
print(inp[:40])
