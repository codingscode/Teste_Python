carro = {'marca': 'fiat', 'ano': 2018, 'preco': 35000, 'cor': 'verde', 'novo': True}

print(carro)
print(carro['preco'])
print(carro.get('cor'))

carro['ano'] = 2020
print(carro)

print('--------------------')
print(carro.keys())

print('--------------------')
print(carro.values())


print('--------------------')
carro['segurado'] = False
print(carro)

print('--------------------')

print(carro.items())

print('--------------------')

if 'marca' in carro:
    print('há a propriedade \'marca\' em carro ')

print('--------------------')
