def main ():
  a = []
  b = []

  print('Digite aqui as coordenadas de a: ')

  for i in range (3):
    aux = float(input())
    a.append(aux)
  
  print ('Digite aqui as coordenadas de b: ')
  for i in range (3):
    aux = float(input())  
    b.append(aux)

  print(a)
  print(b)
    
  res = 0
  for i in range (3):
    res = res + a[i]*b[i]
  print('Produto Escalar: {}'.format(res))
main()