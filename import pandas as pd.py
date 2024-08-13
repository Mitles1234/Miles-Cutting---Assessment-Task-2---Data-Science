from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Sample data
x = np.linspace(-5, 5, 100)
y = np.sin(x)
z = np.cos(x)

ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Sin X')
ax.set_zlabel('Cos X')

plt.show()