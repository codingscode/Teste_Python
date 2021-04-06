# juntando sets
lugares1 = {'teresina', 'recife', 'paraíba'}
lugares2 = {'manaus', 'florianópolis', 'belo horizonte'}
lugares = lugares1.union(lugares2)

print(lugares1)
print(lugares2)
print(lugares)


print('-----------------')
# mesmo com update()

print('-----------------')
# interseção de conjuntos
criterios1 = {'preço', 'qualidade', 'frete', 'garantia', 'comentarios', 'descontos'}
print(criterios1)

criterios2 = {'preço', 'frete', 'design', 'durabilidade'}
print(criterios2)

criterios1.intersection_update(criterios2)
print(criterios1)

print('-----------------')
numeros1 = {1, 3, 9, 11}
numeros2 = {-3, 8, 3, 40, 9, 60}
comum = numeros1.intersection(numeros2)

print(numeros1)
print(numeros2)
print(comum)

print('-----------------')
# excluindo o que é comum

conjunto1 = {'a', 'b', 'c', 'd', 'x', 'y'}
conjunto2 = {'t', 'b', 'k', 'd', 'w', 'y'}

print(conjunto1)
print(conjunto2)

conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)

print('-----------------')
conjunto3 = {'apple', 'banana', 'cherry'}
conjunto4 = {'google', 'microsoft', 'apple'}

print(conjunto3)
print(conjunto4)

z = conjunto3.symmetric_difference(conjunto4)

print(z)

print('-----------------')
