"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

num = float(input('Insira um valor: '))

if num < 0:
    print('Esse número é negativo.')
elif num > 0:
    print('Esse número é positivo.')
else:
    print('Esse número é zero.')
