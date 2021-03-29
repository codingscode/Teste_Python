
valor1 = 5
valor2 = 15


def intervalo(valor):
    if valor < 20 and valor > 13:
        return f'{valor} está dentro do intervalor entre 13 e 20'
    return f'{valor} está fora do intervalor entre 13 e 20'


print(intervalo(valor1))
print(intervalo(valor2))
print('------------------')

x = ['maçã', 'banana']
y = ['maçã', 'banana']
z = x

print(x is z)   # is é para objeto e == é para comparar valores
print(x is y)
print(x == y)

print('------------------')
