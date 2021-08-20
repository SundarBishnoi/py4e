text = "X-DSPAM-Confidence:    0.8475"
sindex = text.find('0')
lindex = text.find('5',sindex)
fvalue = text[sindex:(lindex+1)]
print(float(fvalue))
fruit = 'banana'
letter = fruit[1]
print(letter)
print(len(fruit))
