classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]

upper = []
lower = []

for subject in classes:
    aclass = subject.split()
    if aclass[0] == 'MATH':
        if int(aclass[1]) >= 300 :
            upper.append(subject)
        else : 
            lower.append(subject)

    if aclass[0] == 'ENG' :
        if int(aclass[1]) >= 200 :
            upper.append(subject)
        else : 
            lower.append(subject)

    if aclass[0] == 'PSYCH' :
        if int(aclass[1]) >= 400 :
            upper.append(subject)
        else : 
            lower.append(subject)

print(upper)
print(lower)
print(len(classes))
print(len(upper))
print(len(lower))