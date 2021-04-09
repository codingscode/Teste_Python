# classes/objetos

class Carro:
    preco = 23000  # propriedade
    ano = 2010  # propriedade

print(Carro)
print(Carro.preco)

carro = Carro
print(carro)
print(carro.preco)
print(carro.ano)

print('--------------------------')

class Pessoa:
    # esta funcao é chamada automaticamente
    def __init__(self, nome, profissao):  # o objeto-classe, parametro1, parametro2, ...
        self.nome_pessoa = nome             # objeto-classe.propriedade
        self.profissao_pessoa = profissao   # objeto-classe.propriedade
        self.mostrar_self()

    def mostrar_self(self):
        return f'eu sou self, e meu valor aqui é {self}'


pessoa = Pessoa('Simon', 'Programador')

print(pessoa.nome_pessoa)
print(pessoa.profissao_pessoa)
print(pessoa.mostrar_self())

print('--------------------------')
pessoa.nome_pessoa = 'Picasso'
pessoa.profissao_pessoa = 'Pintor'


print(pessoa)
print(pessoa.nome_pessoa)
print(pessoa.profissao_pessoa)

print('--------------------------')
