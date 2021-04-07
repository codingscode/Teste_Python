produto = {'nome': 'queijo', 'preco': 3.5, 'validade_meses': 3}

print(produto)

produto.update({'preco': 5.0})
print(produto)

produto.update({'marca': 'parmalate'})
print(produto)

print('----------------------')
produto.pop('nome')
print(produto)


print('----------------------')
produto.popitem()
print(produto)

produto.update({'estado': 'liquido'})
produto.update({'desnatado': False})
print(produto)

print('----------------------')
del produto['validade_meses']
print(produto)

print('----------------------')
produto.clear()
print(produto)

print('----------------------')

