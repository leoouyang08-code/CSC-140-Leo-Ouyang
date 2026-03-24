""" thelist = [2, 8, 1, 8, 3]
eightcount = 0
for num in thelist:
    if num == 8:
        eightcount += 1

print(eightcount) """

"""
print("=== Loop Practice Program ===")
nums = [3, -1, 7, 0, 4, -2]
i = 0
positive_count = 0

while i < len(nums):
    if nums[i] > 0:
        positive_count += 1
    i += 1

print("Positive numbers:", positive_count)
# Sum numbers until use enters 0
total = 0
num = int(input("Enter a number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Enter a number (0 to stop): "))

print("Total sum:", total)

# Simple search
target = int(input("Enter a number to search for:"))
i = 0 
found = False

while i < len(nums):
    if nums[i] == target:
        found = True
    i += 1

print("Found?", found)

"""

"""for i in range(6):
    square = i * i
    print(square)

for row in range(3):
    for col in range(3):
        print("(",row,",",col,")",end="")
    print()

for r in range(1, 6):
    for c in range(1,6):
        print(r*c, end="\t")
    print()

for i in range(4):
    for j in range(3):
        print("*", end="")
    print()

for i in range(4):
    for j in range(4):
        print("#", end="")
    print() """

### invariant --> stays true for every iteration
#### loop invariant --> something that remains true everytime the loop repeats

""" total = 0
for x in [1,2,3,4]:
    total += x
print(x)

for i in range(len(names)):
    print(i, names[i]) """

## total remains the sum of all previously processed numbers

"""nums = [1,2,3,4]
for i in range(len(nums)):
    nums[i] *= 2
print(nums)"""

nums = [5, 10, 15]
for i in range(len(nums)):
    nums[i] *= 3
print(nums)

for i in range(1,50):
    print("*" * i)

for i in range(1,6):
    for j in range(1, i+1):
        print(j, end="")
    print()

for r in range(4):
    for c in range(4):
        if (r+c) % 2 == 0:
            print("X", end="")
        else:
            print("O", end="")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(i, end="")
    print()