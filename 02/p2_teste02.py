#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

pontos_y = np.array([3, 8, 1, 10])

plt.plot(pontos_y, marker = 'o')  # ou plt.plot(pontos_y, marker = '*')
plt.show()

""" 
# desnecessario no colab
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
"""

print('------------------------')

pontos_y2 = np.array([4, 9,-3, 14])
plt.plot(pontos_y2, 'o:r')

print('------------------------')

pontos_y3 = np.array([10, 15, 5, 20])
plt.plot(pontos_y3, marker = 'o', ms = 20)  #  plt.plot(pontos_y3, marker = 'o', ms = 20, mec = 'r') ou plt.plot(pontos_y3, marker = 'o', ms = 20, mfc = 'r')
# plt.plot(pontos_y3, marker = 'o', ms = 20, mec = 'r', mfc = 'r')

print('------------------------')
