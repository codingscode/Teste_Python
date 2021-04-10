a = 5  # variavel global
print(f'a = {a}')

def minhafuncao():  # outro escopo
    a = 7  # variavel local 
    print(f'a interno = {a}')


minhafuncao()
print(f'a = {a}')

print('-----------------------')
b = 10 # variavel global
print(f'b = {b}')

def minhafuncao2():
    global b  # fazer variavel local ser variavel global
    b = 12  # variavel global sendo sobrescrita
    print(f'b interno = {b}')


minhafuncao2()
print(f'b = {b}')

print('-----------------------')
