# python -> list;  javascript -> array

carros = list()

print(carros)
print(type(carros))
print(len(carros))

carros.append('celta')
carros.append('corsa')
carros.append('ka')
carros.append('corolla')
carros.append('palio')
carros.append('fiesta')
carros.append('kombi')
carros.append('gol')
print(carros)
print(len(carros))

print('--------------------')
carros.pop() # por padrão remove o último
print(carros)

carros.pop(3) # remove o elemento indice 3
print(carros)

print('--------------------')
carros.remove('fiesta')  # removendo pelo elemento
print(carros)

print('--------------------')
