horas_dias = float(input('Digite aqui quanto você ganha por dia: '))
horas_mes = int(input('Digite aqui as horas trabalhadas por mês: '))
irpf = int(input('Digite aqui o valor (%) do desconto do irpf: '))
inss = int(input('Digite aqui o valor (%) do desconto do inss: '))
contribuicao_sindical = int(input('Digite aqui o valor (%) da contribuição sindical: '))

sal_bruto = horas_dias*horas_mes
sal_liq = (sal_bruto * (irpf/100) * (inss/100) * (contribuicao_sindical/100))*1000
print('O seu salário líquido é de: {:.2f}'.format(sal_liq))