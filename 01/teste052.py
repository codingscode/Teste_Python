# RegEx
import re
from re import search, findall, split, sub

print(dir(re))
# Verificar se a string inicia com 'A' e termina com 'bonita':
texto = 'A rua de paralelepipedo do centro é bonita de se ver'
x = search('^A.*bonita$', texto)

if x:
  print('Sim, há combinação')
else:
  print('Não há combinação')

print('---------------------')
resp = findall('le', texto)
resp2 = findall('bairro', texto)

print(resp)
print(resp2)

print('---------------------')
comb1 = search('\s', texto)
comb2 = search('praça', texto)
comb3 = search('le', texto)

print(comb1.start())
print(f'o 1º espaço em branco está na posição: {comb1.start()}')
print(comb2)
print(comb3)

print('---------------------')
dividir1 = split('\s', texto)
dividir2 = split('e', texto)
dividir3 = split('k', texto)
dividir4 = split('a', texto, 3)

print(dividir1)
print(dividir2)
print(dividir3)
print(dividir4)

print('---------------------')
substituir1 = sub('\s', '*', texto)
substituir2 = sub('\s', '*', texto, 3)

print(substituir1)
print(substituir2)
print('---------------------')
# primeira palavra com 'p', esta palavra seu inicio e fim
procurar1 = re.search(r'\bp\w+', texto)

print(procurar1.span())
print(procurar1.string)
print(procurar1.group())

print('---------------------')
