#program to find largest and smallest number in series entered by user.
largest = None
smallest = None
while True:
    val = input('Enter integer number: ')
    if val == 'done':
        break
    try :
        ival = int(val)
    except:
        print('Invalid input')
        continue
    if largest is None and smallest is None :
        largest = ival
        smallest = ival
    else :
        if largest < ival :
            largest = ival
        if smallest > ival:
            smallest = ival
print('Maximum is', largest)
print('Minimum is', smallest)