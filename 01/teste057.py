# usar colab
import pandas as pd

dados = {
  'calorias': [420, 380, 390, 200, 800],
  'duracao': [50, 40, 45, 68, 3]
}

mostrar1 = pd.DataFrame(dados)

mostrar1

print('-----------------------')
mostrar1.loc[0]

print('-----------------------')
mostrar1.loc[1]

print('-----------------------')
mostrar1.loc[[0, 1]]

print('-----------------------')
dados = {
  'calorias': [420, 380, 390, 200, 800],
  'duracao': [50, 40, 45, 68, 3]
}

mostrar2 = pd.DataFrame(dados, index = ['dia1', 'dia2', 'dia3', 'dia4', 'dia5'])
mostrar2
print('-----------------------')

mostrar2.loc['dia2']

print('-----------------------')
mostrar3 = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')
mostrar3 

print('-----------------------')
