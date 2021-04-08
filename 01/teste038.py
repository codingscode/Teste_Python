# condicionais e statements

a = 7
b = 3

if a > b:
    print('a é maior que b')
elif a < b:
    print('a é menor que b')
else:
    print('a é igual a b')

print('--------------------------')

c = -3
d = 5
e = 8

if d > 0 and c < 3:
    print('ambos são verdadeiros')
else:
    print('pelo menos um é falso')

print('--------------------------')
valor1 = 12
valor2 = -5
valor3 = 6

if valor1 > valor3 or valor3 > 0:
    print('pelo menos um é verdadeiro')
else:
    print('os dois são falsos')

print('--------------------------')
