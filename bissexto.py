ano = int(input('Entre aqui com o ano: '))
if (ano % 400 == 0):
    print('É um ano bissexto!')
elif (ano % 4 == 0):
    print('É um ano bissexto!')
elif (ano % 100 == 0):
    print('Não é um ano bissexto!')
else: 
    print('Não é um ano bissexto')