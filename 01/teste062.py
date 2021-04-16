import pandas as pd


dados = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')


dados
novo_dados = dados.dropna()
novo_dados.to_string()
