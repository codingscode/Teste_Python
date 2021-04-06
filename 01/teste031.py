animais = {'cachorro', 'gato', 'papagaio', 'calango', 'macaco', 'preá', 'garça'}

print(animais)
animais.remove('gato')

print(animais)


print('-------------------')
animais.discard('preá')  # discard() não traz erro se o elemento já não existir
print(animais)

print('-------------------')
animais.pop()
print(animais)


print('-------------------')
animais.clear()
print(animais)

print('-------------------')
