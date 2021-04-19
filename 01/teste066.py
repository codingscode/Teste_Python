import pandas as pd


dados = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')
dados

print('----------------------')

dados.corr()  # ignora valores não numéricos

print('----------------------')
