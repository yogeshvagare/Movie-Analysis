import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import regex as re

# Generate some noisy data
np.random.seed(0)
x = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(x).ravel() + np.random.normal(0, 0.2, x.shape[0])

# Split into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Try different degrees of polynomial regression
degrees = [1, 4, 15]  # Underfit, Good fit, Overfit

plt.figure(figsize=(18, 5))
for i, degree in enumerate(degrees):
    poly = PolynomialFeatures(degree)
    x_train_poly = poly.fit_transform(x_train)
    x_test_poly = poly.transform(x_test)

    model = LinearRegression()
    model.fit(x_train_poly, y_train)
    y_pred = model.predict(x_test_poly)

    plt.subplot(1, 3, i + 1)
    plt.scatter(x, y, color='black', label='Data')
    x_plot = np.linspace(0, 5, 100).reshape(-1, 1)
    y_plot = model.predict(poly.transform(x_plot))
    plt.plot(x_plot, y_plot, color='red', label=f'Degree {degree}')
    plt.title(f'Degree {degree}')
    plt.legend()

plt.tight_layout()
plt.show()