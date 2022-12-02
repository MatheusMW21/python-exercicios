#Declarando variáveis
salario = int(input('Entre aqui com o seu salário: '))
porc = int(input('Entre aqui com o aumento percentual (%): '))

#Comandos
fator_aumento = (porc/100) + 1
salario_novo = salario * fator_aumento

print('Seu salário atual é de R${}, após o aumento de {}% seu salário será de R${}'.format(salario, porc, salario_novo))