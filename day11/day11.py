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
    xs.append(y)
    xs.append(y)

plt.scatter(xs,ys, s=0.5)
plt.axis('equal')
plt.axis('off')
plt.show()


from sympy import (
    symbols, expand, factor, simplify, diff, sin, cos, tan, ln, init_printing, expand_trig
)
init_printing()

x = symbols('x')

""" # 2. Differentiation Examples

# Example A
f = sin(x) * x**2
print("f =", f)
print("f' =", diff(f, x))

# Example B
g = ln(x) / x
print("\ng =", g)
print("g' =", diff(g, x))

#higher powers
print("\nd/dx [x**10 · sin(x)] =", diff(x**10 * sin(x), x))

# different functions
print("\nd/dx [tan(x) · ln(x)]  =", diff(tan(x) * ln(x),  x))

# combined terms
print("\nd/dx [sin(x) + x**3 · cos(x)] =",
      diff(sin(x) + x**3 * cos(x), x))
 """
""" # 3. Algebraic Manipulation

# Expand a binomial
expr1 = (x+2)**4
print("\n(x + 2)**4 expanded =", expand(expr1))

# Factor a polynomial
expr2 = x**3 - 4*x**2 + 4*x
print("x³ - 4x² + 4x factored =", factor(expr2))

# Simplify a rational expression
expr3 = (x**2 - 1) / (x - 1)
print("(x² - 1)/(x - 1) simplified =", simplify(expr3))

# Other modifications
print("\n(x + 3)**6 expanded =",  expand((x + 3)**6))
print("x⁴ - 16 factored =",      factor(x**4 - 16))
print("(x³ - 8)/(x - 2) simplified =", simplify((x**3 - 8)/(x - 2)))

# More exploration
 """
