from numpy import roots, complex128


# Recebe as raízes e formata para float
def formata_raizes(r):
    if isinstance(r[0], complex128):
        return r

    resultado = [float(f'{i:.2f}') for i in r]

    return resultado

# Crindo função para calcular f(x) = 3x³ - 4x² + 2x - 5, passando x
def f(x: float) -> float:
    return 3 * x**3 - 4 * x**2 + 2 * x - 5

print(f'f(3) = 3x³ - 4x² + 2x - 5 = {f(3.0):.2f}')
print(f'f(1.5) = 3x³ - 4x² + 2x - 5 = {f(1.5):.2f}')
print(f'f(10.3) = 3x³ - 4x² + 2x - 5 = {f(10.3):.2f}')

# Usando a função roots de numpy para encontrar as raízes de:
# f(x) = 2x + 1
x = roots([2, 1])
print(f'Raiz de f(x) = 2x + 1 => {formata_raizes(x)}')

# f(x) = x² - 4x + 3
x = roots([1, -4, 3])
print(f'Raízes de f(x) = x² - 4x + 3 => {formata_raizes(x)}')

# f(x) = 3x³ - 11x² + 5x + 3
x = roots([3, -11, 5, 3])
print(f'Raízes de f(x) = 3x³ - 11x² + 5x + 3 => {formata_raizes(x)}')

# f(x) = x² + x + 1
# Por não ter raízes reais, as raízes serão complexas
x = roots([1, 1, 1])
# print(f'Raízes de f(x) = x² + x + 1 => {x}')
print(f'Raízes de f(x) = x² + x + 1 => {formata_raizes(x)}')
