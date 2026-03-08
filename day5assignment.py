numlist = []

integer_input = input("Input an integer; cannot be zero. ")

while integer_input != 0:
    try:
        integer_input = input("Input an integer (0 to stop) ")
        integer = int(integer_input) 
        if integer_input != 0:
            numlist.append(integer)
        else:
            break
    
    except ValueError:
        print("Please enter a valid whole number.")

print(numlist)