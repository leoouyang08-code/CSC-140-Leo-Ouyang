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
# 3. Algebraic Manipulation

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