import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')

df  # aparece todos
df.head()  # aparece só 5 primeiros
df.head(3)  # aparece só 3 primeiros

print('--------------------------------')
df.tail()  # aparece os 5 últimos

print('--------------------------------')
df.info()

print('--------------------------------')
