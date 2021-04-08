def minhafuncao():
    return 'você chamou esta função'


print(minhafuncao())

print('----------------')
# funcao com parametros
def minhafuncao2(parametro1, parametro2):
    return f'o parametro1 recebe o argumento: \'{parametro1}\', o parametro2 recebe o argumento: \'{parametro2}\''


print(minhafuncao2('jiló', 'goiaba'))

print('----------------')
# recebendo quantidade indeterminada de argumentos
def minhafuncao3(*args):
    return f'{args} | tipo: {type(args)}'


def minhafuncao4(**kwargs):
    return f'{kwargs} | tipo: {type(kwargs)}'
    

print(minhafuncao3('oi', 'beleza?', True, 3))
print(minhafuncao3([1, 'oi', 9.3, True]))
print(minhafuncao4(nome = 'vicente', idade = 20, altura = 1.8, massa = 80))

print('----------------')
# parametro com valor padrão
def lugar(valor = 'brasil'):
    return f'eu sou do {valor}'

print(lugar('colombia'))
print(lugar('polonia'))
print(lugar())
print(lugar('canadá'))

print('----------------')
def imprimir_iteravel(iteravel):
    for cada in iteravel:
        print(cada)


imprimir_iteravel([4, 8, 1, 9])

print('----------------')
def recursao(k):
  if(k > 0):
    resultado = k + recursao(k - 1)
    print(resultado)
  else:
    resultado = 0
  return resultado

print("\n\nResultados de Exemplos de Recursão:")
recursao(6)

print('----------------')
