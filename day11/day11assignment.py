from sympy import *
init_printing()

x, a, b = symbols('x a b')

# No. 2:

# Example A
f = sin(x) * x**2
print("f =", f)
print("f' =", diff(f, x))

# Example B
g = ln(x) / x
print("\ng =", g)
print("g' =", diff(g, x))

# No. 3:

# expand
expr1 = (x+2)**4
print("\n(x + 2)**4 expanded =", expand(expr1))

# factor
expr2 = x**3 - 4*x**2 + 4*x
print("x³ - 4x² + 4x factored =", factor(expr2))

# simplify
expr3 = (x**2 - 1) / (x - 1)
print("(x² - 1)/(x - 1) simplified =", simplify(expr3))

# other changes
print("\n(x + 3)**6 expanded =",  expand((x + 3)**6))
print("x⁴ - 16 factored =",      factor(x**4 - 16))
print("(x³ - 8)/(x - 2) simplified =", simplify((x**3 - 8)/(x - 2)))

# No. 4:

# 20 mnis
h = (sin(x)**3 * ln(x)**2) / (cos(x) * exp(x)) #
print("\n--- Complex Derivative ---")
print("h        =", h)
print("h'       =", diff(h, x))
print("\nh' (simplified) =", simplify(diff(h, x)))

# first two are trig additional/subtratcion identities, and the others are sin triple identities
print("sin(a + b) expanded =", expand_trig(sin(a + b)))

print("cos(a - b) expanded =", expand_trig(cos(a - b)))

print("\nsin(3a) expanded =", expand_trig(sin(3*a)))

print("cos(3a) expanded =", expand_trig(cos(3*a)))

"""
Discovery: The most surprising result was that SymPy could instantly expand triple angle identities like sin(3a) = 3sin(a) - 4sin**3(a) and cos(3a) = 4cos**3(a) - 3cos(a) using the expand_trig command.
These identities would usually take a lot of time and effort to derive normally, but it seems the library had it bulit in, which is useful. 
I also found it impressive that SymPy handled the complex derivative of (sin³(x)*ln²(x)) / (cos(x)*eˣ) in seconds, a problem that would take ~20 minutes using quotient & product rules manually.
"""