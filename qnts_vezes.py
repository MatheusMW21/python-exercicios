import random

# gerando uma lista com 20 números aleatórios
a = []
x = random.randint (1, 20)
tam = len(a)
while tam <= 20:
  a.append(x)
  x = random.randint(1,20)
  tam = len(a)
print(a)

# implementando interação com usuário
num = int(input('Insira um número e verifique quantas vezes aparece na lista: '))
cont = 0 
# verificar número na lista
for k in a:
  if (k == num):
    cont += 1
print('{} vezes.'.format(cont))