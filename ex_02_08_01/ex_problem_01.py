#8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

fhand  = open('D:\python\py4e\ex_02_08_01\\romeo.txt')
finalList = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in finalList:
            finalList.append(word)
finalList.sort()
print(finalList)
