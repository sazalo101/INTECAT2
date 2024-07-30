import sympy as sp

x = sp.symbols('x')
f = x**2 - x - 2
f_prime = sp.diff(f, x)
print(f_prime)
