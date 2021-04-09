# lambda : é uma função anonima
minha_funcao = lambda a: a + 10    # lambda parametro(s): retorno
print(minha_funcao(5))

print('------------------')
somar = lambda valor1, valor2: valor1 + valor2

print(somar(3, 4))

print('------------------')
somar2 = lambda *args: sum(args)  # quantidade indefinida de argumentos

print(somar2(3, 4, 5, 6))

print('------------------')
def multiplicar(valor):
  return lambda a : a * valor

duplicar = multiplicar(2)

print(duplicar(11)) # 22

print('------------------')
def dividir(valor1):
    return lambda valor2: valor2 / valor1


print(dividir(4)(6))  # 1.5


print('------------------')
def multiplicar2(valor1):
    return lambda valor2, valor3: valor1*(valor2 + valor3)


print(multiplicar2(3)(7, 5))
print('------------------')
