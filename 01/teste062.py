import pandas as pd


dados = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')

dados
print('------------------')
novo_dados = dados.dropna()
novo_dados

print('------------------')
novo_dados.dropna(inplace = True)
novo_dados

print('------------------')
dados2 = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')
dados2.fillna(130, inplace = True)
dados2

print('------------------')
