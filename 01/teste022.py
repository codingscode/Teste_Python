lista1 = ['Paris', 'viagens', 'Bill Gates', 'computador', 'Milão', 'culinária']
veiculos = ['doblò', 'Fusca', 'combi', 'palio', 'celta', 'Corolla', 'ferrari']



print(lista1)
lista1.sort()  # ordenação sensitiva
print(lista1)

print('---------------------------------')
lista1.sort(key = str.lower)  # ordenação não sensitiva
print(lista1)

print('---------------------------------')
print(veiculos)
veiculos.reverse()
print(veiculos)

print('---------------------------------')
