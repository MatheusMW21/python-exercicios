#var 
qntd_dia = int(input('Insira aqui a quantidade de cigarros que você fuma por dia: '))
qntd_ano = float(input('Insira aqui a quantidade de anos que você fuma: '))

#comandos
reducao_em_minutos = qntd_ano * 365 * qntd_dia * 10 
reducao_em_dias =reducao_em_minutos / (24*60)
print('Redução do tempo de vida {:8.2f} dias.'.format(reducao_em_dias))