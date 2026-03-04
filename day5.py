""" numbers = [10,20,30,40]
student_info = ["Alice", 17, 3.8]
items = []
items.append("Notebook")
items.append("Pencil")
print(items)
print(numbers)
print(student_info) """

""" foods = ["Pho", "Curry", "eel"]
print(foods)

colors = ["red", "green", "blue"]
print(colors[0])
colors[1] = "yellow"
print(colors)
print(colors[-1]) """

""" movies = ["Chainsaw Man: Reze Arc", "Rush Hour", "The Matrix"]
print(movies)
movies[1] = "Yu-Gi-Oh: Dark Side of Dimensions"
print(movies) """

""" scores = [88, 92, 75, 91]
print(len(scores))
print(scores[3])
# print(scores[4]) --> refers to 5th element and not the 4th
print(scores[len((scores))-1]) """


""" prime_numbers = [1, 3, 5, 7, 11]
print(prime_numbers[len(prime_numbers)-1])

animals = ["cats", "dog", "bird"]
for a in animals:
    print(a)
for i in range((len(animals))):
    print(i, animals[i])
total = 0
for n in [2, 4, 6]:
    total += n
print(total) """

"""
names = ["Abraham", "Bill", "Carol"]

for n in names:
    print(n, "is present") """

""" nums = [4, 7, 2, 9]
target = 7
found = False
for n in nums:
    if n == target:
        found = True
print(found) """ 


"""grid = [
    [1,2,3],
    [4,5,6]
]
print(grid[0][1])
print(grid[1][2])
for row in grid:
    for value in row:
        print(value, end="") """

""" grid = [
    ["Apples", "Bananas", "Cherry"],
    ["Dates", "Eggplant", "Fig"] 
        ]
for row in grid:
    for value in row:
        print(value, end=", ") """

""" numbers = [5, 12, 7, 5, 9, 5]

print("Array:", numbers)

count = 0

for n in numbers:
    
    if n == 5:

        count += 1 

print("Number of 5s:", count)

total = 0

for n in numbers:
    
    total += n 

print("Sum:", total)

numbers[2] = 100

print("Modified array:", numbers)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
    [7, 8, 9]
]

print("2D Array")

for row in matrix:
    for val in row:
        print(val, end="")
    print()

count = 1
count = 0
"""
"""
while count <= 5:
    print("Hello", count)
    count += 1

num = 0
"""

"""
while num < 10:
    num += 1
    print(num)

x = 10
while x > 0:
    print(x)
    x -= 1
"""

"""
num = 0

while True:
    try:
        num_input = input("Yo let me get a number ").strip()
        num = int(num_input)

        if num <= 100:
            num_input = input("Yo let me get a number ").strip()
        else: 
            break

    except ValueError:
        print("Please enter a valid number.")
"""
n = 5 
while n>0:
    if n%2 == 0:
        print("even")
    else:
        print("odd")
    n -= 1 

"""odd even odd even odd""" 