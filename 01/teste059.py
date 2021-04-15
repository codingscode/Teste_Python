# usar colab
import pandas as pd
from json import loads, dumps
from urllib.request import urlopen


mostrar1 = pd.read_json('https://raw.githubusercontent.com/codingscode/Teste_Python/master/meu_json.json')
mostrar2 = mostrar1.to_string()

mostrar1
mostrar2

print('--------------------------------')
mostrar3 = mostrar1.head()
mostrar3

print('--------------------------------')
resposta = urlopen('https://raw.githubusercontent.com/codingscode/Teste_Python/master/meu_json.json')
dados_json = loads(resposta.read())
dados_json

print('--------------------------------')
