largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    
    try : 
        fval = float(num)
    except :
        print("Invalid input")
        continue
        
    if largest is None:
        largest = fval
        smallest = fval
    else :
        if fval > largest :
            largest = fval
        if fval < smallest:
            smallest = fval

print("Maximum", largest)
print("Minimum", smallest)