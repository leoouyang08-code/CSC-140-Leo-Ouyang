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

def f(x): 
    return ((math.pi/2 - x)*math.tan(x))

x = []
for i in range(1,400):
    x.append(+i*0.0003)

x_vals = x
y_vals = [f(x) for x in x_vals]
print(y_vals)
plt.plot(x_vals,y_vals)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function")
plt.grid(True)
plt.show()