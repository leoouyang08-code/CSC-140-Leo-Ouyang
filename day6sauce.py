numbers = []

while True:
    try:
        integer_input = input("Input an integer (0 to stop): ")
        integer = int(integer_input)

        if integer == 0:
            break

        numbers.append(integer)

    except ValueError:
        print("Please enter a valid whole number.")

sum = 0
fifty_count = 0
ten_count = 0

for number in numbers:

    if number > 50:
        fifty_count += 1

    if number == 10:
        ten_count += 1

    sum += number

print(fifty_count)
print(sum)

if ten_count >= 1:
    print("Yes it does")

if len(numbers) != 0:
    largest = numbers[0]
    smallest = numbers[0]

minmax = []
number = 0

if len(numbers) != 0:
    while number < len(numbers):
        if numbers[number] > largest:
            largest = numbers[number]
        number += 1
    number = 0
    minmax.append(largest)

    while number > len(numbers):
        if numbers[number] < largest:
            smallest = numbers[number]
        number += 1
    minmax.append(smallest)

    print(largest)
    print(smallest)
    print(minmax)

# the trace
""" input = 10 --> integer = 10 --> numbers = [10] """
""" input = 100 --> integer = 100 --> numbers = [10, 100] """
""" input = 0 --> stops --> numbers = [1, 10, 100] """

