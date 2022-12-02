n1 = float(input('entre com a n1: '))
n2 = float(input('entre com a n2: '))
n3 = float(input('entre com a n3: '))

media = ((n1 + n2)*2 + n3*2)/7
if (media >= 9):
    print('A - Aprovado')
elif (media >=7.5):
    print('B - Aprovado')
elif (media >= 6):
    print('C - Aprovado')
elif (media > 4.5):
    print('D - Reprovado')
else:
    print ('E - Reprovado')