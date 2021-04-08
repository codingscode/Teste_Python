pessoa = { 'nome': 'Fabiola', 'idade': 19, 'massa': 73, 'altura': 1.77, 'uf': 'tocantis' }

print(pessoa)

for cada in pessoa: # só as chaves
    print(cada)

print('---------------------')

for cada in pessoa:
    print(pessoa[cada])  # acessando valores


print('---------------------')

for cada in pessoa.values():  # só os valores
    print(cada)


print('---------------------')

for cada in pessoa.keys():
    print(cada)


print('---------------------')

for cada in pessoa.items():
    print(cada)

print('---------------------')

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

print('---------------------')
