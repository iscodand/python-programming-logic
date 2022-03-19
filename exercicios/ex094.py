"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero 
invertido.

Exemplo:
  12376489
  => 98467321
"""

num = input('\nInsira um número: ')
print(f'\nNúmero: {num}')
num = num[::-1]
print(f'Número invertido: {num}\n')
