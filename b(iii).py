import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def model(x, a, b):
    return a * x + b


x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([1, 4, 9, 16, 25])


params, _ = curve_fit(model, x_data, y_data)
a, b = params


plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model(x_data, a, b), label='Fit', color='red')
plt.legend()
plt.show()
