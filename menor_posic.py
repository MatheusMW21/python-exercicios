import random

# gerando uma lista com números aleatórios
l1 = []
x = random.randint(1, 10)
tam = len(l1)

while tam <= 10:
  l1.append(x)
  x = random.randint(0, 10)
  tam = len(l1)
print(l1)

def menor_posic(l1):
  l2 = []
  menor = l1[0]
  cont = -1
  posic = 0
  for k in l1:
    cont += 1
    if (k < menor):
      menor = k 
      posic = cont
  l2.append(menor)
  l2.append(posic)
  print(l2)
menor_posic(l1)