fhandle = open('D:\python\py4e\ex_02_07_02\\mbox-short.txt')
counts = dict()
for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word,0) + 1

bigCount = None
bigSender = None

for sender, count in counts.items():
    if bigCount is None or count > bigCount :
        bigCount = count
        bigSender =  sender
print(bigSender, bigCount)