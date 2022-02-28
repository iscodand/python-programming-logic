"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento."""

import math

num = float(input('Insira um número ----> '))

if (num // 1 == num):
    print(f'O número {num} é inteiro.')
else:
    print(f'O número {num} é decimal.')