import pandas as pd


dados = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')

dados

dados['data'] = pd.to_datetime(dados['data'])
dados

print('-------------------')
dados.dropna(subset=['date'], inplace = True)
dados



print('-------------------')





print('-------------------')




print('-------------------')
