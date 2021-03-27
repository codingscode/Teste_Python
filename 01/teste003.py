

nome1, nome2, nome3 = ['maria', 'estela', 'ana']

print(nome1)
print(nome2)
print(nome3)
print('---------------')

string1 = 'jun'
string2 = 'tos'

print(string1 + string2)

x = 3  # sou global
print(x)


def funcao():
    x = 4   # sou local
    return x

def funcao2():
    global x  
    x = 10   # estou sobrescrevendo a variavel global
    return x


print(funcao())
print(x)
print(funcao2())
print(x)
print('---------------')

