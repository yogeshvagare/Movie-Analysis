import numpy as np
import matplotlib.pyplot as plt

x = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(x).ravel() + np.random.normal(0, 0.2, x.shape[0])

degrees = [1, 4, 15] 

plt.subplot(1, 3, 2)
plt.scatter(x, y, color='black', label='Data')
x_plot = np.linspace(0, 5, 100).reshape(-1, 1)
y_plot = np.linspace(0, 5, 100).reshape(-1, 1)
plt.plot(x_plot, y_plot, color='red', label=f'Degree {degrees}')
plt.title(f'Degree {degrees}')
plt.legend()

plt.tight_layout()
plt.show()
