import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


dados = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')
dados

print('--------------------------')

dados.plot()

plt.show()



print('--------------------------')

dados2 = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/outros.csv')

dados2  # imprimir
dados2.plot()  # imprimir

print('--------------------------')

dados2.plot(kind = 'scatter', x = 'Duracao', y = 'Calorias')

print('--------------------------')
dados2.plot(kind = 'scatter', x = 'Duracao', y = 'Maxpulso')


""" 
# desnecessario
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

"""

print('--------------------------')
