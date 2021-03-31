frutas = ['banana', 'melancia', 'graviola', 'laranja', 'goiaba', 'maçã', 'jaca']
nova_lista = []


print(frutas)
print(nova_lista)


for cada in frutas:
    nova_lista.append(cada)

print(nova_lista)

print('---------------------------')
roupa = ['camisa', 'calça', 'bermuda', 'saia', 'camiseta', 'palitó', 'vestido']
nova_lista2 = []

print(roupa)
print(nova_lista2)

nova_lista2 = [cada for cada in roupa if 'a' in cada]
print(nova_lista2)

print('---------------------------')

animais = ['macaco', 'raposa', 'aranha', 'coelho', 'cachorro', 'urso', 'baleia']

print(animais)
nova_lista3 = [cada for cada in animais]
print(nova_lista3)

nova_lista4 = ['olá' for cada in animais]
print(nova_lista4)

print('---------------------------')

mais_frutas = ['maça', 'banana', 'pessego', 'kiwi', 'manga']
print(mais_frutas)

nova_lista5 = [cada if cada != 'banana' else 'laranja' for cada in mais_frutas]

print(nova_lista5)

print('---------------------------')
