largest = None
smallest = None
while True:
    the_num = input("Enter digit: ")
    try:
        the_num = int(the_num)
        if largest is None and smallest is None:
            largest = the_num
            smallest = the_num
        else :
            if largest < the_num:
                        largest = the_num
            elif smallest > the_num :
                        smallest = the_num
    except:
        if the_num == "done":
            break
        else : print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
