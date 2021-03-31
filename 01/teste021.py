produtos = ['impressora', 'mouse', 'teclado', 'webcam', 'gabinete', 'monitor']
numeros = [21, 10, 15, 40, 8, 19]


print(produtos)

produtos.sort()  # ordena em ordem alfabetica
print(produtos)

print(numeros)
numeros.sort()   # ordena em ordem numerica
print(numeros)

print('---------------------------------')

produtos.sort(reverse = True)
print(produtos)
numeros.sort(reverse = True)
print(numeros)

print('---------------------------------')

def minhafuncao(n, valor = 50):  # ordena em quão perto o numero está próximo do numero 50
  return abs(n - valor)

lista_numeros = [53, 0, 10, 900, 3, 11]

print(lista_numeros)
lista_numeros.sort(key = minhafuncao)  

print(lista_numeros)

print('---------------------------------')
