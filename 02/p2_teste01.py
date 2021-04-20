# usando colab

import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

pontos_x = np.array([0, 6])
pontos_y = np.array([0, 250])

plt.plot(pontos_x, pontos_y)
plt.show()

""" # desnecessario
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
"""

print('---------------------')

pontos_x2 = np.array([4, 17])
pontos_y2 = np.array([8, 23])

plt.plot(pontos_x2, pontos_y2, 'o')

print('---------------------')

pontos_x3 = np.array([1, 2, 6, 8])
pontos_y3 = np.array([3, 8, 1, 10])

plt.plot(pontos_x3, pontos_y3)

print('---------------------')

pontos_y4 = np.array([3, 8, 1, 10, 5, 7])

plt.plot(pontos_y4)

print('---------------------')
