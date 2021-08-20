hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
def computepay(hours,rate):
    if hours>40:
        gross_pay = 40*rate + (hours-40)*rate*1.5
        return gross_pay
    else :
         gross_pay = hours * rate
         return gross_pay

print("Pay:",computepay(hours,rate))
