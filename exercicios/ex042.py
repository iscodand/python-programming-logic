"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""

num1 = float(input('Insira um número ----> '))
num2 = float(input('Insira mais um número ----> '))

print(
    '\nInsira qual operação você deseja realizar: \n[1] - Adição\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão')
operacao = float(input('\nVocê escolheu ----> '))

if operacao == 1:
    calculo = (num1 + num2)
elif operacao == 2:
    calculo = (num1 - num2)
elif operacao == 3:
    calculo = (num1 * num2)
elif operacao == 4:
    calculo = (num1 / num2)
else:
    print('Opção Inválida.')
    quit()

positivo_negativo = 0
par_impar = 0
inteiro_decimal = 0

if (calculo % 2 == 0):
    par_impar = "par"
else:
    par_impar = "ímpar"
if (calculo > 0):
    positivo_negativo = "positivo"
else:
    positivo_negativo = "negativo"
if (calculo // 1 == calculo):
    inteiro_decimal = "inteiro"
else:
    inteiro_decimal = "decimal"

print(
    f'\nO resultado da operação é {calculo}. Esse número é {par_impar}, {positivo_negativo} e {inteiro_decimal}')
