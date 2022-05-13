"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

num = int(input('Insira um número ----> '))
count = 0
for i in range(2, num):
    if num % i == 0:
        count += 1
if count == 0:
    print('O número é primo.')
else:
    print('O número não é primo.')
