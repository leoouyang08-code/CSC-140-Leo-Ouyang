import math
import matplotlib.pyplot as plt
def f(x):
    return math.tan(x-1)/x

x_vals = []
for i in range(-100, 101):
    if i != 0:
        x_vals.append(i / 10000)

y_vals = [f(x) for x in x_vals]

approach_values = [-0.1, -0.01, -0.001, 0.001, 0.01, 0.1]

for a in approach_values:
    print(a, f(a))

plt.plot(x_vals, y_vals)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Quadratic Function")
plt.grid(True)
plt.show()



