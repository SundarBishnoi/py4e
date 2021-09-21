import re
fhandle1 = open('ex_03_11\\actualData.txt', 'r')
sum = 0
for line in fhandle1:
    y = re.findall('[0-9]+', line)
    if len(y) > 0 :
        for num in y:
            sum = sum + int(num)
    
print(sum)
