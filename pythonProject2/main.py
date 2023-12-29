import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 2*np.pi, 0.01)
y = np.sin(3*x)
y1 = np.sin(2*x)

plt.plot(x, y)
plt.plot(x, y1)

plt.show()
