minha_tupla1 = ('oi', 12, True, 30.43)


print(minha_tupla1)
print(minha_tupla1[0])
print(minha_tupla1[1])
#minha_tupla1[1] = 100    # uma tupla é inalteravel
print(minha_tupla1)
#minha_tupla1[4] = 4
print(minha_tupla1)


print('-----------------------')
cores = ('verde', 'laranja', 'purpura', 'azul', 'branco')  # o que define uma tupla é a vírgula

print(cores)
print(type(cores))
print(len(cores))

print('-----------------------')

nomes = ('fabiola')
lugares = ('bonito',)


print(nomes)
print(type(nomes))
print(lugares)
print(type(lugares))

print('-----------------------')
# convertendo para tupla
lista1 = [10, 'python', 1.5, False]
string1 = 'rua legal'

print(lista1)
print(string1)

minha_tupla2 = tuple(lista1)
minha_tupla3 = tuple(string1)

print(minha_tupla2)
print(minha_tupla3)

print('-----------------------')
