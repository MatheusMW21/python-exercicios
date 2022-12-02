#var
num1 = int(input("Entre com um número: "))
num2 = int(input("Entre com outro número: "))

#comandos
if (num1 > num2):
  print ('{} é maior que {}'.format(num1, num2))
elif (num2 > num1):
  print ('{} é maior que {}'.format(num2, num1))
else:
  print ('Os números são iguais!')