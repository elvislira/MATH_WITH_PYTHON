from math import sin
from math import exp


# f(x) = 2e^(x/2) -3sen(x) + 2x³ - 5
def f(x: float) -> float:
    return 2 * exp(x/2) - 3 * sin(x) + 2 * x**3 - 5

if __name__ == '__main__':
    print(f'f(3.0) = {f(3.0)}')
    