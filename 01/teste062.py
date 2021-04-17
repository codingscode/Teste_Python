import pandas as pd


dados = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')

dados
print('------------------')
novo_dados = dados.dropna()
novo_dados

print('------------------')
dados2 = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')
novo_dados2 = dados2
novo_dados2.dropna(inplace = True)
novo_dados2

print('------------------')
dados3 = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')
dados3.fillna(130, inplace = True)  # celulas vazias serão preenchidas por 130
dados3

print('------------------')






print('------------------')





print('------------------')






print('------------------')






print('------------------')

















