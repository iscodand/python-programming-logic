valor_hora = float(input('Insira o valor que você recebe por hora: '))
horas_mes = float(
    input('Insira o números de horas mensais que você trabalha: '))

salario = valor_hora * horas_mes
print('\nSeu salário bruto é de', salario, 'reais. \n')

inss = salario * 0.08
print('Você paga', inss, 'reais para o INSS. \n')

sindicato = salario * 0.05
print('Você paga', sindicato, 'reais para o Sindicato. \n')

ir = salario * 0.11
print('Você paga', ir, 'reais para o Imposto de Renda. \n')

descontos = inss + sindicato + ir
print('Você tem', descontos, 'reais descontados do seu salário de',
      salario, 'reais mensais. \n')

salario_liquido = salario - descontos
print('Você recebe', salario_liquido, 'reais de Salário Líquido. \n')
