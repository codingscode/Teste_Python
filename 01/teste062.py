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

dados4 = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')
dados4['sobrenome'].fillna('preenchido', inplace = True) # preenche somente os vazios da coluna 'sobrenome'
dados4

print('------------------')

dados5 = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')
coluna_idade = dados5['idade'].median()
coluna_idade
dados5['idade'].fillna(coluna_idade, inplace = True)
dados5

print('------------------')

dados6 = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')
coluna_saldo = dados6['saldo'].mode()[0]  # a moda
dados6['saldo'].fillna(coluna_saldo, inplace = True)  # na coluna saldo valores vazios substitui-se pela 'moda'
dados6

print('------------------')
