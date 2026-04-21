# 2a

"""
(a) State the derivative of g(x) = ln(x). Then use the limit definition of the derivative to plot the numerical derivative on a domain where ln(x) is defined.
(b) Determine the limit of g'(x) as x approaches 0 from the right. Provide the Python code you used to investigate this numerically.
(c) Explain how the graph of the numerical derivative (computed using the limit definition and vectorized code) supports your conclusion in part (b).
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.01, 2, 400)

h = 1e-5

g_x = np.log(x)
g_prime_num = (np.log(x + h) - np.log(x)) / h

plt.figure()
plt.plot(x, g_x, label="g(x) = ln(x)")
plt.plot(x, g_prime_num, '--', label="Numerical derivative")
plt.legend()
plt.title("ln(x) and its Derivative")
plt.show()

# 2b

x_small = np.linspace(1e-6, 0.1, 100)
h = 1e-8

g_prime_small = (np.log(x_small + h) - np.log(x_small)) / h

print(g_prime_small[:10])
