class Carro:

    def __init__(self, v_nome, v_preco, v_ano):
        self.nome = v_nome
        self.preco = v_preco
        self.ano = v_ano

    def mostrar(self):
        return f'{self.nome} | {self.preco} | {self.ano}'


carro1 = Carro('corsa', 29000, 2014)

print(carro1.mostrar())

print('-------------------')

class CarroImplementacao(Carro):
    def __init__(self, v_nome, v_preco, v_ano,v_cor, v_segurado):
        Carro.__init__(self, v_nome, v_preco, v_ano)
        self.cor = v_cor
        self.segurado = v_segurado

    def mostrarmais(self):
        return f'{self.cor} | {self.segurado}'


carromelhori = CarroImplementacao('corolla', 56000, 2019, 'prata', True)

print(carromelhori.mostrar())
print(carromelhori.mostrarmais())

print('-------------------')
class CarroImplementacao2(Carro):
    def __init__(self, v_nome, v_preco, v_ano, v_arcon, v_blindado):
        super().__init__(v_nome, v_preco, v_ano)
        self.arcon = v_arcon
        self.blindado = v_blindado

    def maisinfo(self):
        return f'arcon: {self.arcon} | blindado: {self.blindado}'
    

carro2 = CarroImplementacao2('bmw', 100000, 2017, True, False)

print(carro2.mostrar())
print(carro2.maisinfo())

print('-------------------')
