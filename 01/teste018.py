nomes = ['larissa', 'paula', 'rosa', 'ezequiel', 'felipe', 'césar', 'estela', 'abigail', 'vicente']
cores = ['azul', 'verde', 'vermelho', 'amarelo', 'branco', 'preto', 'purpura']
lugares = ['paris', 'new york', 'barcelona', 'ipanema', 'buenos aires', 'tokyo', 'tel aviv', 'amsterdam']


print(nomes)
nomes.remove('césar')  # remove um elemento específico por vez
print(nomes)
nomes.pop()  # por padrão remove o último elemento
print(nomes)
nomes.pop(2) # remove o elemento indice 2 da nova lista
print(nomes)

print('--------------------------')

print(cores)
del cores[3]  # apaga o elemento indice 3
print(cores)
del cores  # apaga a lista cores inteira
#print(cores)  #

print('--------------------------')
print(lugares)
lugares.clear()  # esvazia a lista
print(lugares)

print('--------------------------')
