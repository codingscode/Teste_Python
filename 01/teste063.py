import pandas as pd


dados = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')

dados

dados['data'] = pd.to_datetime(dados['data'])
dados

print('-------------------')
dados.dropna(subset=['data'], inplace = True)  # tira as que não estam em formato de data
dados

print('-------------------')
