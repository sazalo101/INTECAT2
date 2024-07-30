import scipy.integrate as spi

f = lambda x: x**2 - x - 2
integral, error = spi.quad(f, 1, 3)
print(integral)
