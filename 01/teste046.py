desenhos = ('tom & jerry', 'batman', 'super man', 'scoobidoo', 'dragon ball', 'johnny quest')
meuinterador = iter(desenhos)

print(next(meuinterador))
print(next(meuinterador))
print(next(meuinterador))

print('-------------------')
class MeusNumeros:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

minhaclasse = MeusNumeros()
meuiterador = iter(minhaclasse)

print(next(meuiterador))
print(next(meuiterador))
print(next(meuiterador))
print(next(meuiterador))
print(next(meuiterador))

print('-------------------')
class MeusNumeros2:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 6:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

minhaclasse2 = MeusNumeros2()
meuiterador = iter(minhaclasse2)

for cada in meuiterador:
  print(cada)

print('-------------------')
