# defindo uma função para checagem de numeros primos
print('Digite 10 números e verifique se eles são primos!')
def éPrimo(x):
  fator = 2
  if x == 2:
    return True
  while x % fator != 0 and fator <= x/2:
    fator += 1
    if x % fator == 0:
      return False
    else:
      return True

num = int(input('Digite um número: '))
i = 0
for i in range(1, 10):
  i += 1
  if éPrimo(num):
    print(num, 'é primo!')
  else:
    print(num, 'não é primo :( ')
  num = int(input('Digite um número: '))