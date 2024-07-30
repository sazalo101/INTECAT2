import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])


cs = CubicSpline(x, y)

x_new = np.linspace(1, 5, 100)
y_new = cs(x_new)

plt.plot(x, y, 'o', label='Data')
plt.plot(x_new, y_new, '-', label='Cubic Spline')
plt.legend()
plt.show()
