palavra : str = 'bola'
print(len(palavra))


class Compra:

    def __init__(self: object, produto: str, preco: float, quantidade: int) -> None:
      self.__produto: str = produto
      self.__preco: float = preco
      self.__quantidade: int = quantidade

    @property
    def produto(self: object) -> str:
        return self.__produto

    @property
    def preco(self: object) -> float:
        return self.__preco

    @property
    def quantidade(self: object) -> int:
        return self.__quantidade

    def __str__(self: object) -> str:
        return f'produto: {self.produto}, preço: {self.preco}, quantidade: {self.quantidade}'


compra1: Compra = Compra('caderno', 19.90, 4)
print(compra1)
