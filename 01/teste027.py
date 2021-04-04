tupla1 = ('braço', 'cabeça', 'torax', 'perna')
tupla2 = list(tupla1)


print(tupla1)
print(tupla2)
tupla2[2] = 'barriga'
tupla1 = tuple(tupla2)
print(tupla1)
# em tuplas não se pode adicionar nem remover itens

print('---------------------')
# desenpacotando
musicas = ('pagode', 'rock', 'jazz', 'reggae')
genero1, genero2, genero3, genero4 = musicas

print(musicas)
print(genero1)
print(genero2)
print(genero3)
print(genero4)


print('---------------------')
dias_semana = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']
(dia1, dia2, *restante) = dias_semana



print(dias_semana)
print(dia1)
print(dia2)
print(restante)

print('---------------------')
frutas = ['banana', 'acerola', 'jaca', 'carambola', 'laranja', 'graviola', 'goiaba', 'manga']
(comeco, *meio, ultimo) = frutas


print(frutas)
print(comeco)
print(meio)
print(ultimo)

print('---------------------')
