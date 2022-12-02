import random

# gerando vetor com 20 números aleatórios 
v1 = []
v2 = []
x = random.randint (1, 20)
tam = len(v1)

while tam <= 20:
   v1.append(x)
   x = random.randint(0, 20)
   tam = len(v1)
print('Vetor principal = ', v1)

# gerando vetor com numeros pares

def par(v1):
  v2 = []
  par = 0
  cont = -1
  for i in range(tam):
    cont += 1
    if (v1[i] % 2 == 0):
      par = v1[i]
      v2.append(par)
  print('Vetor com nº pares = ', v2)
par(v1)

def impar(v1):
  v3 = []
  impar = 0
  cont = -1
  for y in range(tam):
    cont += 1
    if (v1[y] % 2 != 0):
      impar = v1[y]
      v3.append(impar)
  print('Vetor com nº ímpares = ', v3)
impar(v1)