estados = ['piauí', 'rio grande do sul', 'sergipe', 'amazonas', 'tocantins', 'pernambuco', 'mato grosso']
transportes = ['bicicleta', 'carro', 'onibus']



print(estados)
print(estados[2:5])
estados[2:5] = ['ceará', 'rio de janeiro', 'minas gerais', 'paraná']  # substitui o trecho
print(estados)
print('------------------------------------')

print(transportes)
transportes.insert(1, 'avião')  # insere 'avião' como 2º elemento
print(transportes)
transportes.insert(3, ('trem', 'navio'))
print(transportes)

print('------------------------------------')

