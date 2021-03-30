minha_lista1 = ['playstation', 'pendrive', 'headset', 'pc', 'monitor', 'som']
cores = ['azul', 'branco', 'amarelo']


print(minha_lista1)
minha_lista1.append('teclado')  # só adiciona um elemento por vez
print(minha_lista1)

#minha_lista1.append('mouse', 'webcam')  #  dá erro

print('------------------------------')
# lista.insert(indice, elemento)  # só adiciona um elemento por vez
print(cores)

cores.extend(['verde', 'laranja', 'roxo'])  # adiciona mais de um elemento de uma vez
print(cores)
cores.extend(('preto', 'bege', 'marrom'))
print(cores)

print('------------------------------')
