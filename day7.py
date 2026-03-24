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

a()