from typing import Counter


jjj = { }
print(type(jjj))

jjj = {'Ramesh' : 12, 'Shyam': 16, 'Hari': 18}
print(jjj)

jjj['Ramesh'] = 55
print(jjj)

jjj['Shyam'] = jjj['Shyam'] + 1
print(jjj)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 5
print(counts)
x = counts.get('Bob',0)
print(x)

print((0,5,3) < (-1, 6 ,3))