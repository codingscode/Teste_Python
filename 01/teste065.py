import pandas as pd
import math


dados = pd.read_csv('https://raw.githubusercontent.com/codingscode/Teste_Python/master/dados.csv')

dados.duplicated()  # remove linhas duplicadas
dados

print('------------------')
