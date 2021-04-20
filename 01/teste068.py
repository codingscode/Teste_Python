import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


dados = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/outros.csv')
dados

print('------------------------')

dados['Duracao'].plot(kind = 'hist')
plt.show()

""" 
# desnecessario
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

"""

print('------------------------')
