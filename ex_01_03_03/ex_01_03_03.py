scr = (input("Enter the score: "))

try :
    score = float(scr)
    if score >= 0.9 and score < 1 :
        print("A")
    elif score >= 0.8 and score < 1 :
        print("B")
    elif score >= 0.7 and score < 1 :
        print("C")
    elif score >= 0.6 and score < 1 :
        print("D")
    elif score < 0.6 :
        print("F")
    else :
        print("Enter the number between 0 and 1")
except :
    print("Enter the number between 0 and 1")
