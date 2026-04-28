"""def greet(name):
    print('I am ' + name + '.')

name = 'leo'

greet(name)"""

## built in functions ##
"""
1. abs(-12)
2. round(3.1415, 3)
print(max())
pow(3,7)

value = min(5,2,9)
print("Minimum value:", value)
"""



"""
value = abs(-20)    
print("Returned value:", value)

import statistics
print(statistics.mean([4,8,12]))

import random
import math
"""

"""
 def triple(n):
    return n * 3

print(triple(2))

def add(a, b):
    return a + b

print(add(10,20)) """

""" def area_square(side):
    return side * side
print(area_square(9)) """

"""
def computing_square(number):
    return number * number


def print_square(square):
    print(square)

square = computing_square(3)

print_square(square)

def a():
    print("Entering A")
    b()
    print("Exiting A")

def b():
    print("Entering B")
    c()
    print("Exiting B")

def c():
    print("Inside C")
    d()

def d():
    print("Inside D")

a()
"""
"""
list_values = []
for i in range(5,51):
    list_values.append(i)

for i in range(len(list_values)):
    if list_values[i] % 5 == 0:
        list_values[i] = 0

print(list_values)


n = 1
x_vals = []
y = 0.1
for i in range(-200,301):
    x_vals.append(i/100)
print(x_vals)
"""

""" def f(x):
   return x**2 - 3*x + 2

x_vals = [i/10 for i in range(-20,21)]
y_vals = [f(x) for x in x_vals] 

print(x_vals) 

plt.plot(x_vals, y_vals)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Quadratic  Function")
plt.grid(True)
plt.show()
"""

"""
import math
import matplotlib.pyplot as plt

def g(x):
   return math.sin(x) + x

x_vals = []
start = -3
end = 3
num_points = 200
step = (end - start) / (num_points - 1)

for i in range(num_points):
   x_vals.append(start + i * step)

g_vals = [g(x) for ]
"""

def h(x):
   return (x**2 - 4)/(x-2)

approach_vals = [1.9, 1.99, 1.999, 2.001, 2.01, 2.1]

for a in approach_vals:
   print(a, h(a))