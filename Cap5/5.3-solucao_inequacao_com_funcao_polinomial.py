from sympy import Poly
from sympy.abc import x
from sympy.solvers.inequalities import solve_poly_inequality


# 3x != 7
solucao = solve_poly_inequality(Poly(3*x-7, x), '!=')
print(f'3x != 7, S={solucao}')

# x² + x <= 6
solucao = solve_poly_inequality(Poly(x**2+x-6, x), '<=')
print(f'x² + x <= 6, S={solucao}')

# x³ - 3x² - 10x + 24 > 0
solucao = solve_poly_inequality(Poly(x**3 - 3*x**2 - 10*x + 24, x), '>')
print(f'x³ - 3x² - 10x > 24, S={solucao}')


## Funções polinomiais modulares
from sympy import Abs
from sympy.solvers.inequalities import reduce_abs_inequalities
# x já importado anteriormente


# |5x + 4| - 3 >= 0
solucao = reduce_abs_inequalities([(Abs(5*x+4)-3, '>=')], x)
print(f'|5x + 4| >= 3, S={solucao}')


