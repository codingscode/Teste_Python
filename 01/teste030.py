produtos = {'play1', 'pendrive', 'tv', 'pc', 'impressora'}


print(produtos)
produtos.add('mouse')
print(produtos)
produtos.add('teclado')
produtos.add('teclado')
print(produtos)

print('--------------------')
frutas1 = {'maça', 'laranja', 'graviola'}
frutas2 = {'goiaba', 'abacaxi', 'tanja'}

print(frutas1)
print(frutas2)

frutas1.update(frutas2)

print(frutas1)

print('--------------------')
# adicionando qualquer iteravel
nomes = {'paulo', 'vicente', }
mais_nomes = ['vitor', 'renan', 'alberto']

nomes.update(mais_nomes)
print(nomes)

print('--------------------')
