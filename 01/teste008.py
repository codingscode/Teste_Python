frase1 = 'Olá, pessoal'
frase2 = 'Raimunda Alves Pinto'
com_espacos = '   veja isto   '
atividade1 = 'Faço caminhada as 17:00'


print(frase1.upper())  # coloca todos caracteres maiusculos
print(frase2.lower())  # coloca todos caracteres minusculos
print(com_espacos)
print(com_espacos.strip())  # tira espaços das extremidades
print(atividade1)
print(atividade1.replace('caminhada', 'natação'))  # substitui uma substring por outra
print('----------------')

frase3 = 'bom dia pessoas'
frase4 = 'saúde, paz, esperança'

print(frase3)
print(frase3.split())  # gera uma lista de substrings cujo criterio de separação é 1 espaço vazio
print(frase4)
print(frase4.split(','))  # gera uma lista de substrings cujo criterio de separação é uma virgula
