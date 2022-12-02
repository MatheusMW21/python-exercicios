h = float(input('Entre aqui com a altura: '))
sexo = input('Qual o sexo? (m/f): ')
if (sexo == 'm'):
    peso = (72.7*h)-58
    print('Peso ideal: {:.3f}kg'.format(peso))
elif (sexo == 'f'):
    peso = (62.1 * h)-44.7
    print('Peso ideal: {:.3f}kg'.format(peso))
else:
    print('Sexo Inválido!')