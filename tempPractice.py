text = "X-DSPAM-Confidence:    0.8475"
fpos = text.find("0")
lpos = text.find("5")
value = text[fpos:lpos+1]
print(float(value))
