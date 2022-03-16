"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que 
peça um número inteiro e determine se ele é ou não um número primo.
"""

num = int(input('Número ----> '))
count = 0

for i in range(2, num):
    if num % i == 0:
        count += 1

if count == 0:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')
