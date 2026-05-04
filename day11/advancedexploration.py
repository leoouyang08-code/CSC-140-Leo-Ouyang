# ── 4. ADVANCED EXPLORATION BLOCK ────────────────────────────
from sympy import *
init_printing()

x, a, b = symbols('x a b')

expr = (2*x**3 - 4*x**2 + 4*x - 8) / (x - 2)

expanded_num = expand(2*x**3 - 4*x**2 + 4*x - 8)
print("\nExpanded numerator:", expanded_num)

factored_num = factor(2*x**3 - 4*x**2 + 4*x - 8)
print("Factored numerator:", factored_num)

simplified_expr = simplify(expr)
print("Simplified expression:", simplified_expr)

val_at_3    = expr.subs(x, 3)
val_at_neg1 = expr.subs(x, -1)
print("Value at x = 3 :", val_at_3)
print("Value at x = -1:", val_at_neg1)

val_at_2 = expr.subs(x, 2)
print("Value at x = 2 (division by 0):", val_at_2)

roots = solve(2*x**3 - 4*x**2 + 4*x - 8, x)
print("Roots of numerator:", roots)