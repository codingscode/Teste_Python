
try:
    print(nao_definido) # nao foi definido
except:
    print('uma exceção ocorreu')

print('-------------------------')

try:
  print(x)
except NameError:
  print('variavel x não está definida')
except:
  print('Algo deu erro')

print('-------------------------')

try:
  print('Olá')
except:
  print('Algo deu errado')
else:
  print('Nada deu errado')

print('-------------------------')

try:
  print(y)
except:
  print('Algo deu errado')
finally:
  print('O \'try except\' terminou')

print('-------------------------')



print('-------------------------')
