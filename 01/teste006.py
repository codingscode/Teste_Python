string1 = 'python'

print(f'string1: {string1}')
print(f'comprimento string1: {len(string1)}')
print(string1[0])
print(string1[1])
print(string1[2])
print('---------------------')

for i in range(len(string1)):
    print(i)


print('---------------------')

for cada in string1:
    print(cada)

print('---------------------')

string2 = 'isto é uma frase'

print('uma' in string2)
print('nada' in string2)
print('frase' not in string2)
print('nada' not in string2)
