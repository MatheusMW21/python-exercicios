#var
km = int(input('Insira aqui a quantidade de kilometros percorridos: '))
dias = int(input('Insira aqui por quantos dias o carro foi alugado: '))

#Comandos
preco_dia = 60*dias
preco_km = 0.15*km
preco = preco_dia + preco_km
print('O preço a pagar é R${}'.format(preco))
