"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120
"""

num = int(input('Insira um valor ----> '))
fact = 1

for i in range(num, 1, -1):
    fact *= i

print(f'O fatorial do número {num} é {fact}.')
