""" import sympy as sp
from sympy import pprint

x, y, z = sp.symbols('x y z')
print(x+x+y+2*y-10*y)

x, y, z = sp.symbols('x y z')
pprint(x+x+y+2*y-10*y)

expr = x**2-9
factored = sp.factorial(expr)
expanded = sp.expand((x - 3)*(x + 3))
factored, expanded
pprint(expr)
pprint(expanded)
pprint(factored) """

""" ##Substitution
import sympy as sp
from sympy import pprint

x, y, z = sp.symbols('x y z')
y = sp.series(sp.sin(x), x, 0, 10)
print(y)
pprint(y)

p = sp.series(sp.cos(x), x, 0, 10)
print(p)
pprint(p)
 """

import sympy as sp
from sympy import pprint
from sympy import FiniteSet

""" x, y, z = sp.symbols('x y z')
sp.solve(x**2 - 5*x + 6, x)
print(sp.solve(x**2 - 5*x + 6, x))
 """
""" a, b, c, x, y = sp.symbols('a b c x y')

A = FiniteSet(1, 2, 3, 4)
B = FiniteSet(3, 4, 5)

union_AB = A.union(B)
intersection_AB = A.intersection(B)
difference_AB = A - B

print(union_AB, intersection_AB, difference_AB) """

import matplotlib.pyplot as plt
import random

A = (0,0)
B = (1,0)
C = (0.5, 0.866)
vertices = [A, B, C]
x, y = 0.2, 0.3
xs = []
ys = []

for _ in range(5000):
    vx, vy = random.choice(vertices)
    x = (x + vx)/2
    y = (y + vy)/2
    xs.append(x)
    xs.append(y)

plt.scatter(xs,ys, s=0.5)
plt.axis('equal')
plt.axis('off')
plt.show()