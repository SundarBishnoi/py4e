def computeGrade(score):
    if score >= 0.9:
        return 'A'
    elif score >=0.8:
        return 'B'
    elif score >=0.7:
        return 'C'
    elif score >=0.6:
        return 'D'
    elif score < 0.6 :
        return 'F'

try:
    x = input('Enter score: ')
    grade = computeGrade(float(x))
    print(grade)
except:
    print('Bad score')
