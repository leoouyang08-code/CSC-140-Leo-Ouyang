""" M = True
print(M, type(M))
y = "hello"
print(len(y))

x = input("yo pass me an int between 17 and 25 exclusive: ")
y = input("Please give me your age: ")
age = int(x) + int(y)
print("You will be a billionare at age " + str(age))
 """

""" a = 4 + 18 // 3 ** 2
b = (4+18) // 3 ** 2
c = 5 + 2 * 3 > 10
d = not False or False and True

print(d) """

a = str(49)
b = float(5.9)
c = True
d = 'Z'

print("a:", a, "type:", type(a))
print("b:", b, "type:", type(b))
print("c:", c, "type:", type(c))
print("d:", d, "type:", type(d))

print("\n=== Type Conversion ===")
age_str = "16"
age_num = int(age_str)
print("age_str:", age_str, "type:", type(age_str))
print("age_num:", age_num, "type:", type(age_num))
print("Next year age:", age_num + 1)

print("\n=== Arithmetic Operators ===")
x = 7
y = 4
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)
print("x % y =", x % y)
print("x ** y =", x ** y)

print("\n=== Relational Operators ===")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

print("\n=== Logical Operators ===")
p = True
q = False
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

print("\n=== Precedence and Associativity ===")
expr1 = 2 + 3 * 4
expr2 = (2 + 3) * 4
expr3 = 2 ** 3 % 2
expr4 = 5 + 2 * 3 > 10
expr5 = not True or False

print("2 + 3 * 4 =", expr1)
print("(2 + 3) * 4 =", expr2)
print("2 ** 3 ** 2 =", expr3)
print("5 + 2 * 3 > 10 =", expr4)
print("not False or False and True =", expr5)

print("\n=== Common Pitfalls ===")
# String and number mixing
score = 95
print("Score:", score)                 # Safe print
print("Score: " + str(score))          # Correct concatenation

# Integer vs float division
print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)

# Comparison vs assignment
n = 10
is_ten = (n == 10)
print("n == 10:", is_ten)

print("\n=== Try Your Own ===")
print("Change values of x, y, a, b, and expressions in this file.")
print("Run the file again after each change and observe the results.")

