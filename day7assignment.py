import math
import matplotlib.pyplot as plt

# double functions
def f(x):
    return math.sin(x)/x

def g(x):
    return abs(x)/x

# creating a domain w/ for loop
x_vals = []
for i in range(-1000, 1001):
    if i != 0:
        x_vals.append(i / 100)

# appending y values
f_vals = [] 
g_vals = []

for x in x_vals:
    f_vals.append(f(x))
    g_vals.append(g(x))

# approach values
approach_vals = [-0.1, -0.01, -0.001, -0.0001, 0.0001, 0.001, 0.01, 0.1]

# printing function values
print("Approaching 0:")

for a in approach_vals:
    print(f"x = {a} -> f(x) = {f(a)}, g(x) = {g(a)}")

# tighter values + graph
tight_x = []

for i in range(-1000, 1001):
    if i != 0:
        tight_x.append(i / 10000)

tight_f = []
tight_g = []

for x in tight_x:
    tight_f.append(f(x))
    tight_g.append(g(x))

# f(x)
plt.figure()
plt.plot(tight_x, tight_f)
plt.title("f(x) = sin(x)/x near x = 0")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()

# g(x)
plt.figure()
plt.plot(tight_x, tight_g)
plt.title("g(x) = |x|/x near x = 0")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.grid()

plt.show()