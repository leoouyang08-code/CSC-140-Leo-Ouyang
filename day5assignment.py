numlist = []

while True:
    try:
        integer_input = input("Input an integer (0 to stop): ")
        integer = int(integer_input)

        if integer == 0:
            break

        numlist.append(integer)

    except ValueError:
        print("Please enter a valid whole number.")

print(numlist)
print(len(numlist))
print(numlist[0])
print(numlist[len(numlist)-1])

all_sum = 0
for i in numlist:
    all_sum += i
print(all_sum)

positive_count = 0
for i in numlist:
    if i > 0:
        positive_count += 1

print(positive_count)

ten_count = 0

for i in numlist:
    if i == 10: 
        ten_count += 1

if ten_count > 0:
    print("Yes, 10 does appear in the list. ")

largest = numlist[0]
number = 0

while number < len(numlist):
    if numlist[number] > largest:
        largest = numlist[number]
    number += 1

print("Largest Number: ", largest)

while len(numlist) < 4:
    numlist.append(0)

matrix = [
    [numlist[0], numlist[1]],
    [numlist[2], numlist[3]]
]

for row in matrix:
    print(row)

## code trace

""" Trace of Input Loop

Iteration 1
User input: 5
integer = 5
numlist = [5]

Iteration 2
User input: -2
integer = -2
numlist = [5, -2]

Iteration 3
User input: 10
integer = 10
numlist = [5, -2, 10]

Iteration 4
User input: 0
integer = 0
Loop stops (break) """