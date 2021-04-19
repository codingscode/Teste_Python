import pandas as pd
import math


dados = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')

dados

print('-------------------')

dados.loc[5, 'idade'] = 17   # na coluna 'idade' no indice 5 recebe o valor '17'
dados

print('-------------------')

dados['idade'][3]


for cada in dados.index:
    if math.isnan(dados.loc[cada, 'idade']):  # na coluna 'idade' valores que não sejam número receberam 21
        dados.loc[cada, 'idade'] = 21

dados

print('-------------------')

for cada in dados.index:
    if dados.loc[cada, 'idade'] > 19:
        dados.drop(cada, inplace = True)

dados

print('-------------------')
