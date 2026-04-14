# a)
## x values are commented out
## x values are given using append instead
## smaller intervals
## Different for loop

# b)
## It is easier to read & understand
## faster

## more control over boundary values 

# 2a) 
# returns specific, chosen values instead
# you get to see both sides

# 2b) 
# getting to see both sides of the limit

import math
import matplotlib.pyplot as plt
import numpy as np

""" def f(x): 
    return x * math.sin(1/x)

x = []
for i in range(1,400):
    x.append(.1-i*0.003)

x_vals = x
y_vals = [f(x) for x in x_vals]
print(y_vals)
plt.plot(x_vals,y_vals)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function")
plt.grid(True)
plt.show() """

""" x = np.linspace(-5,5,400)
f = x**2
print(x,f)
 """
""" 
x = np.linspace(-5,5,400)

f = x**2
g = np.sin(x)
h = np.exp(-x)

plt.plot(x, f, label="f(x) = x^2")
plt.plot(x, g, label="g(x) = sin(x)")
plt.plot(x, h, label="h(x) = e^(-x)")

plt.title("Multiple Functions on One Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.show() """


""" x = np.linspace(-1,1,10000)

f = x*np.sin(1/x)
g = np.absolute(x)
h = -np.absolute(x)

plt.title("Multiple Functions on One Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.show() """

x = np.linspace(0,16.28,10000)

h = .0001
f = np.sin(x)
fxh = np.sin(x+h)
fd = (fxh-f)/h

plt.plot(x, f)
plt.plot(x, fxh)
plt.plot(x, fd)
plt.title("Multiple Functions on One Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.show()