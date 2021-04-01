lista_1 = ['parafuso', 'alicate', 'serra']
lista_2 = ['martelo', 'chave de fenda', 'lixa']
lista_3 = lista_1 + lista_2


print(f'lista_1: {lista_1}')
print(f'lista_2: {lista_2}')
print(f'lista_3: {lista_3}')

print('--------------------------')

veiculos1 = ['corsa', 'celta', 'voyage']
veiculos2 = ['palio', 'gol', 'doblò']


print(f'veiculos1: {veiculos1}')
print(f'veiculos2: {veiculos2}')

for cada in veiculos2:
    veiculos1.append(cada)

print(f'veiculos1: {veiculos1}')

print('--------------------------')
lugares1 = ['curitiba', 'maceió', 'sobral']
lugares2 = ['paraíba', 'porto alegre', 'bonito']

print(f'lugares1: {lugares1}')
print(f'lugares2: {lugares2}')

lugares1.extend(lugares2)
print(f'lugares1: {lugares1}')

print('--------------------------')
