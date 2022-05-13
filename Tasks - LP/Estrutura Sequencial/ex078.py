"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""

num = int(input('Número ----> '))
factorial = 1
numbers = 0

for i in range(num, 1, - 1):
    factorial *= i

print(f'{num}! = {factorial}')
