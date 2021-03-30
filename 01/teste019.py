carros = ['corolla', 'fusca', 'doblò', 'ka', 'uno', 'palio']
estados = ['minas gerais', 'amapá', 'ceará', 'pernambuco']
construcao = ['pá', 'serra', 'tijolo', 'cimento', 'ferro', 'pedra', 'areia']


print(carros)

def meu_loop(iteravel):
    for cada in iteravel:
        print(cada)

meu_loop(carros)

print('---------------------------------')

def meu_loop2(iteravel):
    
    for indice in range(len(iteravel)):
        print(iteravel[indice])

meu_loop2(estados)


print('---------------------------------')

def listar(iteravel):
    indice = 0
    while indice < len(iteravel):
        print(iteravel[indice])
        indice += 1

listar(construcao)

print('---------------------------------')

[print(cada) for cada in estados]


print('---------------------------------')


