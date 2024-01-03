from sympy.abc import x
from sympy import factor


f1 = factor(x**2 + 3*x)
print(f1)

f2 = factor(x**2 +4*x + 4)
print(f2)
