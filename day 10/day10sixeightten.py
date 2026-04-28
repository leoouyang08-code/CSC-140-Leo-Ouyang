import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
print(x)
h = 0.0001

f = (1/3) * x ** 3  + 5
fxh = (1/3) * (x + h) ** 3  + 5
f_prime = (fxh-f)/h

plt.plot(x, f)
plt.plot(x, fxh)
plt.plot(x, f_prime)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.show()

# Judging by the values given from the graph, the likely conclusion that the derivative of f(x) is f'(x) = x^2

