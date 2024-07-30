import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])


model = LinearRegression()
model.fit(X, y)

print(f'Coefficient: {model.coef_[0]}')
print(f'Intercept: {model.intercept_}')
