hours = float(input("Enter the hours:"))
rate = float(input("Rate per hour:"))
if hours > 40 :
    gross_pay = 40*rate
    hours = hours-40
    gross_pay = gross_pay + (hours*rate*1.5)
else :
    gross_pay = hours*rate
print(gross_pay)