""" name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to python I/O.")

user_input = input("Enter an integer: ")

if user_input.isdigit():
    value = int(user_input)
    print(f"You entered the integer {value}.")
else:
    print("That is not a valid integer.") """

""" item = "Notebook"
item1 = "Potato"
item2 = "Fancy Potato"
price = 2.49
price1 = 12
price2 = 18.99
print(f"Item: {item:<15} | Price: ${price:>10.2f}")
print(f"Item: {item1:<15} | Price: ${price1:>10.2f}")
print(f"Item: {item1:<15} | Price: ${price2:>10.2f}") """

with open("notes.txt", "a") as f:
    f.write("Another line added safely.\n")