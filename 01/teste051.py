from json import loads, dumps


# string json
string_json = '{"nome": "Vicente", "idade": 21, "uf": "tocantins", "altura": 1.7}'
print(f'string_json: {string_json}')

# json -> dicionario
para_dicionario = loads(string_json)
print(f'para_dicionario: {para_dicionario}')
print(type(para_dicionario))
print(para_dicionario['nome'])
print(para_dicionario['uf'])

print('-----------------------------')
# dicionario python
carro = {'nome': 'gol', 'cor': 'azul', 'ano': 2009, 'preco': 21756.8, 'seguro': False}
print(f'carro: {carro}')
print(type(carro))

# dicionario -> json
para_json = dumps(carro)
print(f'para_json: {para_json}')
print(type(para_json))

print('-----------------------------')
print(dumps({'nome': 'Tom', 'idade': 30}))
print(dumps(['goiaba', 'bananas']))
print(dumps(('goiaba', 'bananas')))
print(dumps('olá'))
print(dumps(42))
print(dumps(31.76))
print(dumps(True))
print(dumps(False))
print(dumps(None))

print('-----------------------------')
dados = {
  'nome': 'Benjamin',
  'idade': 30,
  'casado': True,
  'divorciado': False,
  'filhos': ('Tom','Tsahi'),
  'animais': None,
  'carros': [
    {'model': 'BMW 230', 'mpg': 27.5},
    {'model': 'Ford Edge', 'mpg': 24.1}
  ]
}

print(dumps(dados))

print('-----------------------------')
print(dumps(dados, indent=4))

print('-----------------------------')
print(dumps(dados, indent=4, separators=(". ", " = ")))

print('-----------------------------')
print(dumps(dados, indent=4, sort_keys=True))

print('-----------------------------')
