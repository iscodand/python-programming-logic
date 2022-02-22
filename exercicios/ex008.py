"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

valor = float(input('Insira o valor que você ganha por hora: '))
horas = float(input('Insira o valor de horas que você trabalha por mês: '))

salario = valor * horas

print('Você recebe', salario, 'reais trabalhando', horas, 'horas por mês')
