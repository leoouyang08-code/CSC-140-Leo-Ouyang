""" (a) State the derivative of f(x) = e^x. Then use the limit definition of the derivative:
f'(x) ≈ (f(x + h) - f(x)) / h
to plot the numerical derivative over a reasonable domain.
(b) Explain how you can identify the derivative graphically by comparing the graph of f(x) and the graph of your numerical derivative.
(c) Provide vectorized Python code that computes and plots the numerical derivative using the limit definition. Your code must be fully vectorized (no loops).

 """

# (1a) Define the function & known derivatives
# Derivative of e^x is itself

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,400)
h = 1e-5

# (1c)
f_x = np.exp(x)

f_prime_num = (np.exp(x+h) - np.exp(x))/h

plt.figure()
plt.plot(x, f_x, label="f(x) = e^x")
plt.plot(x, f_prime_num, '--', label="Numerical derivative")
plt.legend()
plt.title("f(x) and its Derivative")
plt.show()

# (2a)
# g(x) = ln(x)
# g'(x) = 1/x

