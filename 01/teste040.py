carros = ['celta', 'gol', 'uno', 'ka', 'vectra', 'doblò']

for cada in carros:
    print(cada)
    if cada == 'ka':
        break

print('----------------')
for cada in carros:
    if cada == 'uno':
        break
    print(cada)

print('----------------')
for cada in carros:
    if cada == 'ka':
        continue
    print(cada)

print('----------------')
print(list(range(8)))

for cada in range(8):
    print(cada)

print('----------------')
print(list(range(3, 8)))  # inicio, fim-1
print(list(range(4, 12, 2)))  # inicio, fim-1, passo

print('----------------')
for cada in range(3, 20, 4):
    print(cada)
else:
    print('finalmente terminado')

print('----------------')
for cada in range(7):
    if cada == 3: break
    print(cada)
else:
    print('finalmente terminado')

#If the loop breaks, the else block is not executed.

print('----------------')
cores = ['vermelho', 'azul', 'verde']
carros2 = ['corsa', 'celta', 'uno']

for cada1 in carros2:
  for cada2 in cores:
    print(cada1, cada2)

print('----------------')
