n1 = int(input('Entre aqui com um número: '))
if(n1 % 2 == 0) and (n1 % 3 == 0):
    print('É divisível por 2 e 3')
elif (n1 % 2 == 0) and (n1 % 3 != 0):
    print('É divisível somente por 2')
elif (n1 % 3 == 0) and (n1 % 2 != 0):
    print('É divisível somete por 3')
else:
    print('Não é divisível nem por 2 e nem por 3')